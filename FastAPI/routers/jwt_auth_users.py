from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# .venv\Scripts\activate acceso al entorno virtual
# el servidor se inicia con: python -m uvicorn FastAPI.routers.jwt_auth_users:app --reload

ALGORITHM = 'HS256'
ACCESS_TOKEN_DURATION = 1
SECRET = '950c00acbaace3a1f6ab4604b602e259bd56e651265b5ebfe58c3f0cc797defd'

router = APIRouter(prefix='/jwtauth', tags=['jwtauth'], responses={status.HTTP_404_NOT_FOUND: {'message': 'Interfaz NO encontrada'}})

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt = CryptContext(schemes=['bcrypt'])

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool


class UserDB(User):
  password: str


users_db = {
    'phurtado': {
      'username':'phurtado', 
      'full_name':'Pablo Hurtado', 
      'email':'phurtado1112@gmail.com', 
      'disabled':False,
      'password':'$2a$12$ez.S6p5Ry5GX4gA8JqrWLefNzTlsN5Go8n2ZQ9rHuZM/19W3BBHy.'
      },
    'ihurtado': {
      'username':'ihurtado', 
      'full_name':'Isabel Hurtado', 
      'email':'ihurtado2412@gmail.com', 
      'disabled':True,
      'password':'$2a$12$J8UhxeW/sref03zat/rXR.N94esj/X2hj5fgcD7vjFaTS499IXg6G'
      }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
  exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
  
  try:
    username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get('sub')
    if username is None:
       raise exception
  except JWTError:
     raise exception
  
  return search_user(username)
  
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user
    
@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

    expire = datetime.utcnow() + access_token_expiration

    access_token = {'sub':user.username, 'exp':expire}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "JWT"}

@router.get('/users/me')
async def me(user: User = Depends(current_user)):
  return user