from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return '¡Hola FastAPI Pablo!'

@app.get('/url')
async def url():
  return {'url':'https://phdsystems.net', 'nombre':'Pablo'}