from fastapi import FastAPI
from FastAPI.routers import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# .venv\Scripts\activate acceso al entorno virtual
# el servidor se inicia con: python -m uvicorn FastAPI.main:app --reload
# El sitio se ejecuta en: http://127.0.0.1:8000
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount('/static', StaticFiles(directory='FastAPI/static'), name='static')

@app.get('/')
async def root():
  return '¡Hola Pablo soy FastAPI!'

@app.get('/url')
async def url():
  return {'url':'https://phdsystems.net', 'nombre':'Pablo'}