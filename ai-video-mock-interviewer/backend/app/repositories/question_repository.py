from app.repositories import BaseRepository
from app.models import InterviewQuestion

class InterviewQuestionRepository(BaseRepository[InterviewQuestion]):
    model=InterviewQuestion
