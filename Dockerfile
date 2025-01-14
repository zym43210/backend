FROM python:3.8-slim as base

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libpq-dev \
    '^postgresql-client-.+$' \
    gettext

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install "poetry==1.1.4"
COPY pyproject.toml poetry.lock ./
RUN poetry install

EXPOSE 8000

CMD ["./docker-entrypoint.sh"]
