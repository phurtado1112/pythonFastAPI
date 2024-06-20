from fastapi import FastAPI
from FastAPI.routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# el servidor se inicia con: python -m uvicorn FastAPI.main:app --reload
# El sitio se ejecuta en: http://127.0.0.1:8000

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', StaticFiles(directory='FastAPI/static'), name='static')

@app.get('/')
async def root():
  return '¡Hola Pablo soy FastAPI!'

@app.get('/url')
async def url():
  return {'url':'https://phdsystems.net', 'nombre':'Pablo'}