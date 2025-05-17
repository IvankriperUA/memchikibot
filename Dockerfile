FROM python:3.11-slim

WORKDIR /app

COPY Memchiki_bot.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "Memchiki_bot.py"]