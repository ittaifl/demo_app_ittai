# The first stage builds the frontend
FROM node:14 as frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# The second stage builds the backend
FROM python:3.9 as backend
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ ./

# Add ffmpeg and credentials to the backend
COPY /path/to/ffmpeg-6.0-essentials_build/bin/ffmpeg /app/ffmpeg
COPY /path/to/deom-for-interview-b0a1bb/my-service-account-key.json /app/credentials.json

# The third stage puts it all together
FROM python:3.9-slim
WORKDIR /app

COPY --from=frontend /app/build /app/frontend/build
COPY --from=backend /app /app

# Add ffmpeg to the PATH
ENV PATH="/app:${PATH}"

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
