import uuid
from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class InterviewSession(Base):
    __tablename__="interview_sessions"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    livekit_room_name: Mapped[str]=mapped_column(String(255), unique=True, index=True)
    job_title: Mapped[str]=mapped_column(String(255))
    job_description: Mapped[str]=mapped_column(Text)
    experience_level: Mapped[str]=mapped_column(String(100))
    status: Mapped[str]=mapped_column(String(50), default="created", index=True)
    interview_plan: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    final_score: Mapped[float|None]=mapped_column(Float, nullable=True)
    final_report: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    started_at: Mapped[datetime|None]=mapped_column(DateTime(timezone=True), nullable=True)
    ended_at: Mapped[datetime|None]=mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    user=relationship("User", back_populates="sessions")
