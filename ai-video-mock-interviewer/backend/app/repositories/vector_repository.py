from app.repositories import BaseRepository
from app.models import DocumentChunk

class DocumentChunkRepository(BaseRepository[DocumentChunk]):
    model=DocumentChunk
