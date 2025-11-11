# Use the official lightweight Python 3.12 image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir boto3

# Define the default command to run your script
CMD ["python", "aws_automation_manager.py"]
