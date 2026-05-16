import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class FileAsset(Base):
    __tablename__="file_assets"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True, index=True)
    session_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), nullable=True, index=True)
    file_name: Mapped[str]=mapped_column(String(255))
    file_type: Mapped[str]=mapped_column(String(100))
    mime_type: Mapped[str]=mapped_column(String(120))
    s3_key: Mapped[str]=mapped_column(String(500))
    s3_url: Mapped[str|None]=mapped_column(String(500), nullable=True)
    metadata: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
