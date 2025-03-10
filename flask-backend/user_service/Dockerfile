FROM python:latest

WORKDIR /app

COPY flask-backend/user_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask-backend/user_service/ .
COPY flask-backend/common/ ./common

EXPOSE 5001

CMD ["python", "app.py"]
