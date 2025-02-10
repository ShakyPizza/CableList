# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ /app/backend/

# Expose port
EXPOSE 5000

# Start Flask
CMD ["python", "backend/app.py"]
