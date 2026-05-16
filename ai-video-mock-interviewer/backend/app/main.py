from fastapi import FastAPI
from app.routes.router import api_router
from app.core.config import settings

app=FastAPI(title="AI Video Mock Interviewer")
app.include_router(api_router,prefix=settings.api_prefix)
