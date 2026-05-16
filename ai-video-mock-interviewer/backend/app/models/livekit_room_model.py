import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class LivekitRoom(Base):
    __tablename__="livekit_rooms"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), index=True)
    room_name: Mapped[str]=mapped_column(String(255), unique=True)
    participant_identity: Mapped[str]=mapped_column(String(255))
    metadata: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
