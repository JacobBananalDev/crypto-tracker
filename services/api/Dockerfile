# ------------------------------------------------------------
# Backend Dockerfile
#
# This container runs the FastAPI application.
#
# In production environments, FastAPI apps are typically
# deployed using Uvicorn or Gunicorn inside Docker containers.
# ------------------------------------------------------------

# Use official Python runtime
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for better Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]