from app.repositories import BaseRepository
from app.models import InterviewEvent

class InterviewEventRepository(BaseRepository[InterviewEvent]):
    model=InterviewEvent
