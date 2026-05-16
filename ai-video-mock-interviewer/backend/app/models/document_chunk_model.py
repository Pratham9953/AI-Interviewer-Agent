import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector
from app.core.database import Base

class DocumentChunk(Base):
    __tablename__="document_chunks"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), ForeignKey("documents.id"), index=True)
    chunk_text: Mapped[str]=mapped_column(Text)
    embedding: Mapped[list[float]|None]=mapped_column(Vector(1536), nullable=True)
    metadata: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
