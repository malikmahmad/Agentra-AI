from google.cloud.devtools import cloudbuild_v1
import os

PROJECT_ID = "starlit-lotus-469819-s5"
KEY_PATH = "service-account-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

def check_build():
    client = cloudbuild_v1.CloudBuildClient()
    request = cloudbuild_v1.ListBuildsRequest(
        project_id=PROJECT_ID,
        page_size=1
    )
    builds = client.list_builds(request=request)
    
    for build in builds:
        print(f"Build ID: {build.id}")
        print(f"Status: {build.status}")
        for step in build.steps:
            print(f"Step: {step.name}")
        # Build logs are in GCS usually
        print(f"Log URL: {build.log_url}")
        break

if __name__ == "__main__":
    check_build()
