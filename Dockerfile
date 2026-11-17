FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --only-binary :all: --require-hashes -r requirements.txt

COPY backend/ ./backend/

RUN groupadd --system app \
    && useradd --system --gid app --create-home app \
    && chown -R app:app /app

USER app

WORKDIR /app/backend

EXPOSE 8000

CMD ["gunicorn", "AutoParts.wsgi:application", "--bind", "0.0.0.0:8000"]
