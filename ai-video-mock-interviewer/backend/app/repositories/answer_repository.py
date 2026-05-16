from app.repositories import BaseRepository
from app.models import InterviewAnswer

class InterviewAnswerRepository(BaseRepository[InterviewAnswer]):
    model=InterviewAnswer
