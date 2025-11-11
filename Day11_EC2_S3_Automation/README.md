# ☁️ Day 11 – EC2 & S3 Automation + Logging

## 🎯 Goals
- Automate **EC2 instance start/stop** operations using boto3.
- Upload files to **S3 buckets** programmatically.
- Add **logging** to record each operation (time, action, result).
- Understand how Python scripts interact with AWS resources through `boto3.resource()`.

---

## 🧠 What I Learned

### 1️⃣ EC2 Resource Access
- Used `boto3.session.Session(profile_name='default')` to manage AWS credentials.
- Connected to EC2 and retrieved all instances:
  ```python
  for instance in ec2.instances.all():
      print(instance.id, instance.state['Name'])
  ```

### 2️⃣ Get Instance Name Tag
```
def get_instance_name(instance):
    if instance.tags:
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    return None
```
### 3️⃣ Start / Stop Instance
```
def start_instance(instance_id):
    instance = ec2.Instance(instance_id)
    state = instance.state['Name']
    if state == 'stopped':
        instance.start()
        instance.wait_until_running()
        instance.reload()
        print(f"{instance.id} started → {instance.state['Name']}")
    else:
        print("The instance is currently running.")
```
```
def stop_instance(instance_id):
    instance = ec2.Instance(instance_id)
    state = instance.state['Name']
    if state == 'running':
        instance.stop()
        instance.wait_until_stopped()
        instance.reload()
        print(f"{instance.id} stopped → {instance.state['Name']}")
    else:
        print("The instance is already stopped.")
```
### 4️⃣ S3 File Upload
```
def upload_file(file_path, bucket_name, object_key=None):
    if object_key is None:
        import os
        object_key = os.path.basename(file_path)
    s3.Bucket(bucket_name).upload_file(file_path, object_key)
    print(f"Uploaded {file_path} → s3://{bucket_name}/{object_key}")
```
### 🪵 Logging
```
import logging
logging.basicConfig(
    filename='aws_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```
### Each start/stop/upload action writes an entry into aws_automation.log, e.g.:
```
2025-11-11 14:23:54,031 - INFO - start_instance called: i-0d0c06486b6e1b27d, current_state=stopped
2025-11-11 14:24:10,782 - INFO - instance started: i-0d0c06486b6e1b27d, new_state=running
```
### 🧩 Example Output
```
EC2: i-0d0c06486b6e1b27d running MySecondEC2
S3: scott-boto3-demo-bucket
S3: scott-static-site-demo
[before] i-0d0c06486b6e1b27d state = running, name = MySecondEC2
The instance is currently running.
Uploaded: test.txt  →  s3://scott-boto3-demo-bucket/test.txt
```
### 🏁 Summary

Learned how to manage multiple AWS services in one script.

Practiced object-oriented resource access (ec2.Instance, s3.Bucket).

Added robust logging for traceability.

Verified automation with both running/stopped EC2 states and successful S3 uploads.