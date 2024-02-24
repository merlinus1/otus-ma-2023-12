ARG PYTHON_VERSION=3.11.8

FROM python:${PYTHON_VERSION}-slim AS builder

ENV POETRY_VIRTUALENVS_IN_PROJECT=1

COPY /app/ /app/app
COPY docker/entrypoint.sh /app
COPY pyproject.toml /app

WORKDIR /app

RUN pip install poetry==1.6.1
RUN poetry install --only main


FROM python:${PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY --from=builder /app /app

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]