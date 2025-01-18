FROM python:3.10-slim

WORKDIR /app

COPY docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../crawlers /app/crawlers

COPY . .

WORKDIR /app/crawlers

ENV PYTHONPATH="${PYTHONPATH}:/app/crawlers"

CMD ["python", "crawlers/main.py"]