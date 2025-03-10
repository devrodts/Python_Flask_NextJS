WORKDIR /app

COPY user_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY user_service/ .
COPY commom/ ./common

EXPOSE 5001

CMD ["python", "app.py"]
