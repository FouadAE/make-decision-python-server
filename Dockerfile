# Use the official Python image from the Docker Hub
FROM python:3.12.6

# Prevent Python from writing bytecode (.pyc files)
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent buffering of stdout/stderr in Docker
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.router:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]