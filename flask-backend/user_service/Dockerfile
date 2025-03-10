WORKDIR /app

COPY user-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY user-service/ .
COPY common/ ./common

EXPOSE 5001

CMD ["python", "app.py"]
