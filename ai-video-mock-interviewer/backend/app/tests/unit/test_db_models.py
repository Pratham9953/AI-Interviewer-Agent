import uuid
import pytest
from sqlalchemy import text
from app.core.database import AsyncSessionLocal
from app.repositories.user_repository import UserRepository

@pytest.mark.asyncio
async def test_db_connection_and_user_create():
    async with AsyncSessionLocal() as db:
        result = await db.execute(text('SELECT 1'))
        assert result.scalar() == 1
        repo = UserRepository(db)
        user = await repo.create(email=f"u-{uuid.uuid4()}@x.com", name='u')
        assert str(user.id)
        got = await repo.get(user.id)
        assert got.email == user.email
