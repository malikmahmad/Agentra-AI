from google.cloud import logging
import os

PROJECT_ID = "starlit-lotus-469819-s5"
KEY_PATH = "service-account-key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

def list_logs():
    client = logging.Client()
    # List entries takes a filter
    entries = client.list_entries(
        filter_='resource.type="cloud_run_revision" AND resource.labels.service_name="agentra-backend"',
        order_by="timestamp desc",
        page_size=20
    )
    
    print(f"Fetching logs for {PROJECT_ID}...")
    for entry in entries:
        print(f"[{entry.timestamp}] {entry.severity}: {entry.payload}")

if __name__ == "__main__":
    list_logs()
