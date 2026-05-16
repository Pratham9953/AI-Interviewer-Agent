from app.repositories import BaseRepository
from app.models import LivekitRoom

class LivekitRoomRepository(BaseRepository[LivekitRoom]):
    model=LivekitRoom
