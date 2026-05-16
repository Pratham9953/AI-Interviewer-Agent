from app.repositories import BaseRepository
from app.models import Document

class DocumentRepository(BaseRepository[Document]):
    model=Document
