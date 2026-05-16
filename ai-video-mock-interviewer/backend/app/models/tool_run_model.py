import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ToolRun(Base):
    __tablename__="tool_runs"
    id: Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True), ForeignKey("interview_sessions.id"), nullable=True, index=True)
    tool_name: Mapped[str]=mapped_column(String(120), index=True)
    input: Mapped[dict]=mapped_column(JSONB)
    output: Mapped[dict|None]=mapped_column(JSONB, nullable=True)
    latency_ms: Mapped[int|None]=mapped_column(Integer, nullable=True)
    status: Mapped[str]=mapped_column(String(50), index=True)
    error_message: Mapped[str|None]=mapped_column(Text, nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True), server_default=func.now())
