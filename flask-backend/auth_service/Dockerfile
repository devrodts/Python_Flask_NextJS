FROM python:3.9-slim

WORKDIR /app

COPY auth-service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY auth-service/ .

COPY common/ ./common

EXPOSE 5000

CMD ["python", "app.py"]
