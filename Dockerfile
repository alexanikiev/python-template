# Use a lightweight Alpine-based Python image
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code inside the container
COPY src/ /app/

# Set the default working directory to src/
WORKDIR /app

# Set the entrypoint to run the Python script
CMD ["python", "main.py"]
