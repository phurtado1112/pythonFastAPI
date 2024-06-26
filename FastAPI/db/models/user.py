# Crar la entidad de User

# from bson import ObjectId
from pydantic import BaseModel, Field
# from typing import Optional

class User(BaseModel):
  # id: ObjectId
  # id: str
  id: str = Field(..., alias="_id")
  username: str
  email: str

  class Config:
        validate_assignment = False