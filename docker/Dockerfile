# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set workdir
WORKDIR /app

# Copy only requirements to cache dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Copy backend code
COPY backend ./backend

# Expose port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"] 