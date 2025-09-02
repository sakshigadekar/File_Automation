FROM python:3.12-slim

WORKDIR /app

COPY file_manager/ ./file_manager/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "file_manager/main.py"]

