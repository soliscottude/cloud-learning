# 🧠 Day 10 – boto3 & AWS Connection

## 🎯 Goals
- Install and configure **boto3**, the AWS SDK for Python.  
- Use boto3 to connect to AWS and list S3 buckets / EC2 instances.  
- Understand how local Python scripts interact with cloud resources via the AWS API.  

---

## 🧩 Steps & Commands

### 1️⃣ Install boto3
pip3 install boto3


---

### 2️⃣ List all S3 Buckets

**File:** `boto3_list_buckets.py`

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

print("✅ Your S3 Buckets:")
for bucket in response['Buckets']:
print(f" - {bucket['Name']}")

**Run:**
python3 boto3_list_buckets.py

**Output example:**
✅ Your S3 Buckets:
scott-static-site-demo
scottyang-test-bucket


---

### 3️⃣ Create a New Bucket

**File:** `create_bucket.py`

import boto3

s3 = boto3.client('s3')

bucket_name = "scott-boto3-demo-bucket"

try:
s3.create_bucket(
Bucket=bucket_name,
CreateBucketConfiguration={"LocationConstraint": "ap-southeast-2"}
)
print(f"✅ Created bucket: {bucket_name}")
except Exception as e:
print(f"❌ Error: {e}")

**Run:**
python3 create_bucket.py

**Confirm the new bucket:**
aws s3 ls


---

## 🧠 What I Learned
- boto3 is the official AWS SDK for Python.  
- Local Python scripts can perform real cloud operations through AWS APIs.  
- boto3 automatically uses credentials from `aws configure`.  
- Every boto3 action equals an AWS API call over HTTPS.
