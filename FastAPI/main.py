from fastapi import FastAPI

app = FastAPI()

# el servidor se inicia con: python -m uvicorn FastAPI.main:app --reload

@app.get('/')
async def root():
  return '¡Hola FastAPI Pablo!'

@app.get('/url')
async def url():
  return {'url':'https://phdsystems.net', 'nombre':'Pablo'}