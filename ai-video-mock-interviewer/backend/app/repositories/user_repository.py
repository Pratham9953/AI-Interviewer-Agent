from app.repositories import BaseRepository
from app.models import User

class UserRepository(BaseRepository[User]):
    model=User
