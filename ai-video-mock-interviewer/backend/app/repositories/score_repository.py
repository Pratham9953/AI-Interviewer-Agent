from app.repositories import BaseRepository
from app.models import InterviewScore

class InterviewScoreRepository(BaseRepository[InterviewScore]):
    model=InterviewScore
