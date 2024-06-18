from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# el servidor se inicia con: python -m uvicorn FastAPI.users:app --reload

# Crar la entidad de User

class User(BaseModel):
  name: str
  surname: str
  url: str
  age: int

users_list = [User(name='Pablo', surname='Hurtado', url='https://phdsystems.net', age=60),
         User(name='Antonio', surname='Díaz', url='https://adsystems.net', age=20),
         User(name='Martha', surname='Díaz', url='https://mdsystems.net', age=45)]


@app.get('/usersjson')
async def usersjson():
  return [{'name':'Pablo', 'surname':'Hurtado', 'url':'https://phdsystems.net', 'age':60},
          {'name':'Antonio', 'surname':'Díaz', 'url':'https://adsystems.net', 'age':20},
          {'name':'Martha', 'surname':'Díaz', 'url':'https://mdsystems.net', 'age':45},
          ]

@app.get('/usersclass')
async def usersclass():
  return User(name='Pablo', surname='Hurtado', url='https://phdsystems.net', age=60)

@app.get('/users')
async def users():
  return users_list