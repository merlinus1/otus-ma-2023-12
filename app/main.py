from fastapi import FastAPI

from app.api import health

app = FastAPI(
    title="otus-ma-2023-12",
    openapi_url="/openapi.json",
    docs_url="/docs",
)
app.include_router(health.router)
