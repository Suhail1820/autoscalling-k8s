# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY cpu_task.py .

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "cpu_task.py"]
