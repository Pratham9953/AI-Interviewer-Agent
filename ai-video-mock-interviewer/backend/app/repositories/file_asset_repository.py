from app.repositories import BaseRepository
from app.models import FileAsset

class FileAssetRepository(BaseRepository[FileAsset]):
    model=FileAsset
