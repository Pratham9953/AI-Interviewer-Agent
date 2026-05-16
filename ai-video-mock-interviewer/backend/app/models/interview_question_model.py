import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func, Index
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class InterviewQuestion(Base):
    __tablename__="interview_questions"
    __table_args__=(Index("ix_questions_session_order","session_id","order_index"),)
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), index=True)
    question_text: Mapped[str]=mapped_column(Text)
    skill: Mapped[str|None]=mapped_column(String(120), nullable=True)
    difficulty: Mapped[str|None]=mapped_column(String(50), nullable=True)
    expected_signals: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    order_index: Mapped[int]=mapped_column(Integer, default=0)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
