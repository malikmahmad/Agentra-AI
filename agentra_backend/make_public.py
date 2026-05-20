from google.cloud import run_v2
from google.iam.v1 import policy_pb2
import os

PROJECT_ID = "starlit-lotus-469819-s5"
REGION = "us-central1"
SERVICE_NAME = "agentra-backend"
KEY_PATH = "service-account-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

def make_public():
    client = run_v2.ServicesClient()
    resource = f"projects/{PROJECT_ID}/locations/{REGION}/services/{SERVICE_NAME}"
    
    print(f"Making {SERVICE_NAME} public...")
    
    try:
        # Use positional for resource
        policy = client.get_iam_policy(resource=resource) # Try again without GetIamPolicyRequest
        
        binding = policy_pb2.Binding(
            role="roles/run.invoker",
            members=["allUsers"]
        )
        policy.bindings.append(binding)
        
        client.set_iam_policy(resource=resource, policy=policy)
        print("SUCCESS: Service is now public.")
    except Exception as e:
        print(f"Failed again: {e}")
        print("Trying with dictionary request...")
        try:
             client.set_iam_policy({"resource": resource, "policy": {"bindings": [{"role": "roles/run.invoker", "members": ["allUsers"]}]}})
             print("SUCCESS with dict request.")
        except Exception as e2:
             print(f"Failed dict request: {e2}")

if __name__ == "__main__":
    make_public()
