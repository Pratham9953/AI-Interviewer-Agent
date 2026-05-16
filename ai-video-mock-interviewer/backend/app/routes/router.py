from fastapi import APIRouter
from app.routes.health_routes import router as health
from app.routes.auth_routes import router as auth
from app.routes.interview_routes import router as interviews
from app.routes.livekit_routes import router as livekit
from app.routes.document_routes import router as docs
from app.routes.report_routes import router as reports
from app.routes.websocket_routes import router as ws
api_router=APIRouter()
for r in [health,auth,interviews,livekit,docs,reports,ws]: api_router.include_router(r)
