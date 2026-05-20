FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable for Google Credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json

EXPOSE 8080

# Use shell form to allow environment variable expansion
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
