# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# We use --no-cache-dir to keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Hugging Face Spaces uses port 7860 by default
EXPOSE 7860

# Command to run the application
# We use python app.py but ensure app.py is updated to listen on 0.0.0.0:7860
CMD ["python", "app.py"]
