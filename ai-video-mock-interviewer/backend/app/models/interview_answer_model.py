import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, Text, Float, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class InterviewAnswer(Base):
    __tablename__="interview_answers"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), index=True)
    question_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_questions.id"), nullable=True)
    transcript: Mapped[str]=mapped_column(Text)
    duration_seconds: Mapped[int|None]=mapped_column(Integer, nullable=True)
    confidence_score: Mapped[float|None]=mapped_column(Float, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
