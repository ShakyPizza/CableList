# Use Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend/ /app/backend/

# Expose the correct port
EXPOSE 5000

# Start the Flask server
CMD ["python", "backend/app.py"]
