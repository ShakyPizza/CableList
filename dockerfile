# Use Python for backend
FROM python:3.10

# Set working directory
WORKDIR /app

# Install backend dependencies
COPY backend/ /app/backend/
RUN pip install -r backend/requirements.txt

# Install Node.js and React dependencies
RUN apt-get update && apt-get install -y nodejs npm
WORKDIR /app/frontend
COPY frontend/ /app/frontend/
RUN npm install && npm run build

# Serve React frontend using Flask
WORKDIR /app/backend
CMD ["python", "app.py"]
