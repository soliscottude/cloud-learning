# 🚀 Day 13 – CI/CD with GitHub Actions

## 🎯 Goal
- Understand how **GitHub Actions** automates workflows.
- Build a simple CI/CD pipeline that deploys code to an **AWS S3** bucket automatically.

---

## Frontend(CloudFront)

https://d3hd4jq824wa7l.cloudfront.net

## 🧩 What I Did
1. Created a workflow file at **`.github/workflows/deploy.yml`** in the root directory.  
2. Configured AWS credentials using **GitHub Secrets** (`AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`).  
3. On every push (or manual trigger), GitHub automatically:
   - Checks out my code.
   - Connects to AWS.
   - Runs `aws s3 sync` to deploy my project folder to S3.
4. Verified the upload through the Action logs and the S3 console.

---

## 📄 Workflow Summary
```yaml
name: Deploy to S3
on:
  push:
    branches: [ main ]
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-southeast-2
      - name: Sync to S3
        run: |
          aws s3 sync Day13_CICD_GitHub_Actions s3://scott-static-site-demo
```

## 🧠 Key Takeaways
GitHub Actions runners can execute any AWS CLI or Python script automatically.

```.github/workflows/ ``` must be at the repository root, not inside a subfolder.

Secrets protect sensitive credentials while allowing automation.

CI/CD means: Code push → automatic deployment → no manual upload needed.`

## 🖼 Screenshots

### ✅ Workflow Success

![Workflow Success](./screenshot.png)

### ☁️ Files Uploaded to S3

![S3 Bucket](./screenshot1.png)

### 🌐 CloudFront Test
![CloudFront Page](./screenshot2.png)

## 🧭 Note on CloudFront Caching
After deploying updates to S3, changes may not appear immediately on the CloudFront URL.
This is because CloudFront uses edge caching to speed up delivery by storing copies of content.
You can either:
1. Wait for the cache to expire (usually within 24 hours), or
2. Manually refresh it by creating an Invalidation in the CloudFront console (/*).

✅ The new files are already in S3 — CloudFront just needs time (or a manual refresh) to fetch the latest version.