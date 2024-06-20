from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# el servidor se inicia con: python -m uvicorn FastAPI.users:app --reload

# Crar la entidad de User

class User(BaseModel):
  id: int
  name: str
  surname: str
  url: str
  age: int

users_list = [User(id=1,name='Pablo', surname='Hurtado', url='https://phdsystems.net', age=60),
         User(id=2,name='Antonio', surname='Díaz', url='https://adsystems.net', age=20),
         User(id=3,name='Martha', surname='Díaz', url='https://mdsystems.net', age=45)]


@router.get('/usersjson')
async def usersjson():
  return [{'name':'Pablo', 'surname':'Hurtado', 'url':'https://phdsystems.net', 'age':60},
          {'name':'Antonio', 'surname':'Díaz', 'url':'https://adsystems.net', 'age':20},
          {'name':'Martha', 'surname':'Díaz', 'url':'https://mdsystems.net', 'age':45},
          ]

@router.get('/usersclass')
async def usersclass():
  return User(name='Pablo', surname='Hurtado', url='https://phdsystems.net', age=60)

@router.get('/users')
async def users():
  return users_list

@router.get('/users/{id}')
async def users(id: int):
  return search_user(id)

# @app.get('/userers/')
# async def users(id: int):
#   return search_user(id)

def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return 'Error: Ne se ha encotrado el usuario'
  
@router.post('/users/',status_code=201)
async def user(user: User):
  if type(search_user(user.id)) == User:
    raise HTTPException(status_code=204, detail='El usuario ya existe')
    # return 'Error: El usuario ya existe'
  else:
    users_list.append(user)

  return user

@router.put('/user/')
async def user(user: User):
  found = False
  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True

  if not found:
    return {'Error':'No se ha actualizado el usuario'}
  
  return user

@router.delete('/users/{id}')
async def user(id: int):
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]