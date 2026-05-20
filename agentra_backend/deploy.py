import os
import zipfile
import time
from google.cloud import storage
from google.cloud.devtools import cloudbuild_v1
from google.cloud import run_v2
import google.auth

PROJECT_ID = "starlit-lotus-469819-s5"
REGION = "us-central1"
SERVICE_NAME = "agentra-backend"
BUCKET_NAME = f"{PROJECT_ID}-deploy-source"
KEY_PATH = "service-account-key.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

def zip_source():
    print("Zipping source code...")
    zip_path = "source.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Skip virtual environments and caches
            if 'venv' in root or '__pycache__' in root or '.git' in root or '.artifacts' in root:
                continue
            for file in files:
                if file == zip_path or file == 'deploy.py' or file.endswith('.apk') or file.endswith('.bat'):
                    continue
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, '.'))
    return zip_path

def upload_to_gcs(zip_path):
    print(f"Uploading {zip_path} to gs://{BUCKET_NAME}...")
    client = storage.Client()
    try:
        bucket = client.get_bucket(BUCKET_NAME)
    except:
        bucket = client.create_bucket(BUCKET_NAME, location=REGION)
    
    blob = bucket.blob(zip_path)
    blob.upload_from_filename(zip_path)
    return f"gs://{BUCKET_NAME}/{zip_path}"

def build_image(source_uri):
    print("Triggering Cloud Build...")
    client = cloudbuild_v1.CloudBuildClient()
    # Use unique tag to avoid caching issues
    tag = int(time.time())
    image_uri = f"gcr.io/{PROJECT_ID}/{SERVICE_NAME}:{tag}"
    
    build = cloudbuild_v1.Build()
    build.source = cloudbuild_v1.Source(storage_source=cloudbuild_v1.StorageSource(
        bucket=BUCKET_NAME,
        object="source.zip"
    ))
    
    step1 = cloudbuild_v1.BuildStep(
        name="gcr.io/cloud-builders/docker",
        args=["build", "-t", image_uri, "."]
    )
    step2 = cloudbuild_v1.BuildStep(
        name="gcr.io/cloud-builders/docker",
        args=["push", image_uri]
    )
    
    build.steps = [step1, step2]
    
    operation = client.create_build(project_id=PROJECT_ID, build=build)
    print("Waiting for build to complete...")
    result = operation.result()
    return image_uri

def deploy_to_run(image_uri):
    print(f"Deploying to Cloud Run: {SERVICE_NAME}...")
    client = run_v2.ServicesClient()
    
    parent = f"projects/{PROJECT_ID}/locations/{REGION}"
    
    service = run_v2.Service()
    service.template = run_v2.RevisionTemplate()
    service.template.timeout = "300s"
    container = run_v2.Container()
    container.image = image_uri
    container.resources = run_v2.ResourceRequirements(
        limits={"memory": "1Gi", "cpu": "1"}
    )
    # Cloud Run uses port 8080 by default in my Dockerfile
    container.ports = [run_v2.ContainerPort(container_port=8080)]
    service.template.containers = [container]
    
    # Allow unauthenticated access for simplicity in hackathon
    # Note: Setting IAM policy might be needed separately if client doesn't support it directly in create_service
    
    try:
        operation = client.create_service(parent=parent, service=service, service_id=SERVICE_NAME)
        print("Waiting for deployment to complete...")
        result = operation.result()
    except Exception as e:
        if "already exists" in str(e):
            print("Service already exists, updating...")
            service_path = f"{parent}/services/{SERVICE_NAME}"
            service.name = service_path
            operation = client.update_service(service=service)
            print("Waiting for update to complete...")
            result = operation.result()
        else:
            raise e
            
    # Make service public
    try:
        from google.iam.v1 import policy_pb2
        iam_client = client.get_iam_policy(resource=result.name)
        binding = policy_pb2.Binding(
            role="roles/run.invoker",
            members=["allUsers"]
        )
        iam_client.bindings.append(binding)
        client.set_iam_policy(resource=result.name, policy=iam_client)
        print("Service is now PUBLIC.")
    except Exception as e:
        print(f"Warning: Could not make service public automatically: {e}")
        print("You may need to allow 'allUsers' for 'Cloud Run Invoker' in Google Cloud Console.")

    return result.uri

if __name__ == "__main__":
    try:
        zip_file = zip_source()
        source_uri = upload_to_gcs(zip_file)
        image_uri = build_image(source_uri)
        service_url = deploy_to_run(image_uri)
        print(f"\nSUCCESS! Your backend is live at: {service_url}")
        
        with open("cloud_url.txt", "w") as f:
            f.write(service_url)
            
    except Exception as e:
        print(f"Deployment failed: {e}")
