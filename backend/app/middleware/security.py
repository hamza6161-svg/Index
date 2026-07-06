from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from typing import Dict
import time


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        return response


class SimpleRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 120):
        super().__init__(app)
        self.max_requests = max_requests
        self._store: Dict[str, Dict] = {}

    async def dispatch(self, request: Request, call_next):
        client = request.client.host if request.client else "unknown"
        now = int(time.time())
        window = now // 60
        key = f"{client}:{window}"
        state = self._store.get(key, {"count": 0})
        state["count"] += 1
        self._store[key] = state
        if state["count"] > self.max_requests:
            return Response(status_code=429, content="Too Many Requests")
        response = await call_next(request)
        return response
