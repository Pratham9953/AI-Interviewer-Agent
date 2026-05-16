from typing import Generic, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelT = TypeVar("ModelT")


class BaseRepository(Generic[ModelT]):
    model = None

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, obj_id):
        return await self.db.get(self.model, obj_id)

    async def list(self, limit: int = 100, offset: int = 0):
        result = await self.db.execute(select(self.model).limit(limit).offset(offset))
        return result.scalars().all()

    async def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def update(self, obj, **kwargs):
        for k, v in kwargs.items():
            setattr(obj, k, v)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, obj):
        await self.db.delete(obj)
        await self.db.commit()
