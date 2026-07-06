from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import health
from app.middleware.security import SecurityHeadersMiddleware, SimpleRateLimitMiddleware
from app.database.connection import init_engine

app = FastAPI(title="Global Smart Zone - Shop Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(SimpleRateLimitMiddleware, max_requests=settings.RATE_LIMIT_PER_MINUTE)


@app.on_event("startup")
async def startup():
    init_engine(settings)


@app.get("/version")
async def version():
    return {"app": "Global Smart Zone", "version": "0.1.0"}


app.include_router(health.router, prefix="/api")
