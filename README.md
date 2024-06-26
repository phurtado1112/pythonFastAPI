# Prácticas del curso "Curso de Backend con FastAPI y MongoDB"
## Impartido por MoureDev en YouTube
### En el enlace https://www.youtube.com/watch?v=_y9qQZXE24A

En el curso se tratan crear una API en Python accediendo a una base de datos de MongoDB:

Para ejecutar la aplicación se requiere instalar las librerías que se encentran en el archivo requirements.txt

Es necesario instalar un servidor local de MongoDB Community Edition en local que ejecuta en el servidor:puerto localhost:27017

Para acceder al servidor necesitas el comonado python -m uvicorn FastAPI.main:app --reload

Se necesita ejecutar el request http://127.0.0.1:8000/userdb con:
  1) No Authentication Selected
  2) Body con formato JSON 
   ```
      {
        "username": "usuario",
        "email": "usuario@gmail.com"
      }`
  ```
###### Realizado por **Pablo Hurtado**