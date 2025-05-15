# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the backend code into the container
COPY backend /app/backend

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "/app/backend/app.py"]
