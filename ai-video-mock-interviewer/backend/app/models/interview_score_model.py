import uuid
from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class InterviewScore(Base):
    __tablename__="interview_scores"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), index=True)
    question_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_questions.id"), nullable=True)
    answer_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_answers.id"), nullable=True)
    technical_accuracy: Mapped[int]=mapped_column(Integer)
    clarity: Mapped[int]=mapped_column(Integer)
    depth: Mapped[int]=mapped_column(Integer)
    relevance: Mapped[int]=mapped_column(Integer)
    confidence: Mapped[int]=mapped_column(Integer)
    overall_score: Mapped[float]=mapped_column(Float)
    missing_points: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    red_flags: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    feedback: Mapped[str|None]=mapped_column(Text, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
