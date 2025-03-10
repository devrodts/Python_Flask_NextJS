FROM python:latest

WORKDIR /app

COPY flask-backend/auth_service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY flask-backend/auth_service/ .

COPY flask-backend/common/ ./common

EXPOSE 5000

CMD ["python", "app.py"]
