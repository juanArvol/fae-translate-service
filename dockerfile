FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV ARGOS_PACKAGES_DIR=/app/argos-packages
ENV ARGOS_DEVICE_TYPE=cpu
ENV ARGOS_CHUNK_TYPE=MINISBD
ENV ARGOS_COMPUTE_TYPE=int8_float32

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY models ./models
COPY install_models.py .

RUN python install_models.py

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]