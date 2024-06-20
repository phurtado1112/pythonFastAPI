from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

# el servidor se inicia con: python -m uvicorn FastAPI.routers.basic_auth_users:app --reload

class User(BaseModel):
  id: int
  username: str
  full_name: str
  email: str
  disabled: bool


class UserDB(User):
  password: str


user_db = {
    'phurtado': {
      'username':'phurtado', 
      'full_name':'Pablo Hurtado', 
      'email':'phurtado1112@gmail.com', 
      'disabled':False,
      'password':'123456'},
    'ihurtado': {
      'username':'ihurtado', 
      'full_name':'Isabel Hurtado', 
      'email':'ihurtado2412@gmail.com', 
      'disabled':True,
      'password':'654321'}
}

def search_user(username: str):
  if username in user_db:
    return UserDB(user_db[username])
  
async def current_user(token: str = Depends(oauth2)):
  user = search_user(token)

  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credencial de autenticación inválida', headers={'WWW-Authenticate':'Bearer'})
  return user
  
@app.post('/login')
async def  login(form: OAuth2PasswordRequestForm = Depends()):
  user_db = user_db.get(form.username)
  if not user_db:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El usuario es inválido')
  
  user = search_user(form.username)
  if not form.password == user.password:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El usuario es invalido')
  
  return {'access_token': user.username, 'token_type':'bearer'}

@app.get('/users/me')
async def me(user: User = Depends(current_user)):
  return user