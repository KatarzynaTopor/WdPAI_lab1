# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR C:\Users\kasia\Desktop\WdPAI\lab_1\python_server\server.py

# Copy the Python server script into the container
COPY server.py .

# Expose the port that your Python server will run on
EXPOSE 8000

# Run the Python server
CMD ["python", "./server.py"]