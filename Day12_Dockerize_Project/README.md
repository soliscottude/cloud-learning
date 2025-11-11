# 🐳 Day 12 – Dockerize Your Python Project

## 🎯 Goals
- Containerize the **AWS Automation Manager** (from Day 11) using Docker.  
- Understand how Docker images and containers work.  
- Run the automation script inside a container and publish the image to Docker Hub.

---

## 🧩 Project Structure

```
Day12_Dockerize_Project/
├── aws_automation_manager.py # Script from Day 11
├── Dockerfile # Image build instructions
├── README.md # Learning record
```


---

## ⚙️ Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir boto3
CMD ["python", "aws_automation_manager.py"]
```

## 🚀 Build and Run

### 1️⃣ Build the Image
```
docker build -t aws_automation:v1 .
```

### 2️⃣ Run the Container (with AWS credentials)
```
docker run --rm --name automation-demo \
  -v ~/.aws:/root/.aws:ro \
  -e AWS_PROFILE=default \
  -e AWS_DEFAULT_REGION=ap-southeast-2 \
  aws_automation:v1
```

### ✅ Output example:
```
EC2: i-0d0c06486b6e1b27d stopped MySecondEC2
S3: scott-boto3-demo-bucket
S3: scott-static-site-demo
S3: scottyang-test-bucket
```

## 🧰 Optional Commands
```
# 🧱 List all Docker images
docker images

# 📦 List all containers (including stopped ones)
docker ps -a

# 📜 View logs of a running or exited container
docker logs -f automation-demo

# ⛔ Stop a container
docker stop automation-demo

# ❌ Remove a container (force)
docker rm -f automation-demo

# 🧽 Remove a specific image
docker rmi <image_name>

# 🧹 Clean up dangling intermediate layers
docker image prune -f

# 💣 Remove everything not in use (⚠️ Be careful)
docker system prune -a
```

## 📦 Publish to Docker Hub
```
docker tag aws_automation:v1 soliscottude/aws-automation:v1
docker login
docker push soliscottude/aws-automation:v1
```
🔗 Docker Hub: https://hub.docker.com/r/soliscottude/aws-automation

## 🧹 Cleanup
```
docker rmi aws_automation:v1 nginx:trixie-perl
docker image prune -f
```

## ✅ Results

Successfully built and ran Dockerized aws_automation_manager.py.

Verified EC2/S3 actions via container logs.

Uploaded image to Docker Hub for future deployment and CI/CD integration.

Practiced basic image management and cleanup commands.