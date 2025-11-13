import boto3
import logging
import os
from botocore.exceptions import ClientError

aws_management_console = boto3.session.Session(
    region_name=os.getenv("AWS_DEFAULT_REGION", "ap-southeast-2")

)
ec2 = aws_management_console.resource('ec2')
s3 = aws_management_console.resource('s3')

# Logging

logging.basicConfig(
    filename = 'aws_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# confirming connection successfully

for instance in ec2.instances.all():
    name = None
    if instance.tags:
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                name = tag['Value']
    print('EC2: ', instance.id, instance.state['Name'], name)

for bucket in s3.buckets.all():
    print('S3: ', bucket.name)

# Get instance Name
def get_instance_name(instance):
    if instance.tags:
        for t in instance.tags:
            if t.get('Key') == 'Name':
                return t.get('Value')
    return None

# Function: Start instance when it's stopped

def start_instance(instance_id):
    instance = ec2.Instance(instance_id)
    state = instance.state['Name']
    logging.info(f"start_instance called: {instance_id}, current_state={state}, name={get_instance_name(instance)}")
    print(f"[before] {instance.id} state = {state}, name = {get_instance_name(instance)}")
    
    if state == 'stopped':
        try:
            instance.start()
            instance.wait_until_running()
            instance.reload()
            logging.info(f"instance started: {instance_id}, new_state={instance.state['Name']}")
            print(f"[after ] {instance.id} state = {instance.state['Name']}")
        except ClientError as e:
            logging.error(f"start_instance failed: {instance_id}, error={e}")
            print(f"Error: {e}")
    else:
        logging.info(f"instance already running: {instance_id}")
        print("The instance is currently running.")

# Stop instance when it's running

def stop_instance(instance_id):
    instance = ec2.Instance(instance_id)
    state = instance.state['Name']
    logging.info(f"stop_instance called: {instance_id}, current_state={state}, name={get_instance_name(instance)}")
    print(f"[before] {instance.id} state = {state}, name = {get_instance_name(instance)}")

    if state == 'running':
        try:
            instance.stop()
            instance.wait_until_stopped()
            instance.reload()
            logging.info(f"instance stopped: {instance_id}, new_state={instance.state['Name']}")
            print(f"[after ] {instance.id} state = {instance.state['Name']}")
        except ClientError as e:
            logging.error(f"stop_instance failed: {instance_id}, error={e}")
            print(f"Error: {e}")
    else:
        logging.info(f"instance already stopped: {instance_id}")
        print("The instance is already stopped.")

# Upload files to S3

from botocore.exceptions import ClientError

def upload_file(file_path, bucket_name, object_key = None):
    try:
        if object_key is None:
            import os
            object_key = os.path.basename(file_path)
        
        s3.Bucket(bucket_name).upload_file(file_path, object_key)
        logging.info(f"uploaded file: local={file_path}, s3=s3://{bucket_name}/{object_key}")
        print(f"Uploaded: {file_path}  →  s3://{bucket_name}/{object_key}")
    except ClientError as e:
        logging.error(f"upload failed: local={file_path}, bucket={bucket_name}, key={object_key}, error={e}")
        print(f"Upload failed: {e}")

# Run the functions

if __name__ == "__main__":
    instance_id = os.getenv("INSTANCE_ID")
    bucket_name = os.getenv("BUCKET_NAME")
    file_path = os.getenv("FILE_PATH")

    # --- EC2 Start ---
    if instance_id and os.getenv("START_INSTANCE") == "1":
        # start_instance(instance_id)
        print(f"[INFO] (Simulation) Starting EC2 instance: {instance_id}")

    # --- EC2 Stop ---
    if instance_id and os.getenv("STOP_INSTANCE") == "1":
        # stop_instance(instance_id)
        print(f"[INFO] (Simulation) Stopping EC2 instance: {instance_id}")

    # --- S3 Upload ---
    if bucket_name and file_path and os.getenv("UPLOAD_FILE") == "1":
        # upload_file(file_path, bucket_name)
        print(f"[INFO] (Simulation) Uploading {file_path} → {bucket_name}")

    if not any([instance_id, bucket_name]):
        print("No operations requested. Set environment variables to run AWS actions.")

    print("AWS actions are commented out for safety.")