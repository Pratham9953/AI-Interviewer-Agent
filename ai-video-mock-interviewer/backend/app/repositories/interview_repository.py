from app.repositories import BaseRepository
from app.models import InterviewSession

class InterviewSessionRepository(BaseRepository[InterviewSession]):
    model=InterviewSession
