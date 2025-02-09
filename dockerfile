# Use Python for the Flask backend
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install backend dependencies
COPY backend/ /app/backend/
RUN pip install -r backend/requirements.txt

# Install Node.js & React dependencies
RUN apt-get update && apt-get install -y nodejs npm
WORKDIR /app/frontend
COPY frontend/ /app/frontend/
RUN npm install && npm run build

# Move React build files to Flask static folder
WORKDIR /app/backend
RUN mkdir -p backend/static
RUN cp -r /app/frontend/build/* /app/backend/static/

# Expose the port Flask runs on (important for Railway)
EXPOSE 5000

# Start Flask backend
CMD ["python", "app.py"]
