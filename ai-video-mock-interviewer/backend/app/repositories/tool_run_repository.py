from app.repositories import BaseRepository
from app.models import ToolRun

class ToolRunRepository(BaseRepository[ToolRun]):
    model=ToolRun
