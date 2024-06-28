# Crar la entidad de User

from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    username: str
    email: str