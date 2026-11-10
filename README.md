# Proyecto Docker: Flask + MySQL

Proyecto académico de dos servicios:
- `app`: API web en Python/Flask.
- `db`: base de datos MySQL.

## Requisitos
- Docker Desktop instalado y en ejecución.
- Git.
- Cuenta de GitHub para publicar el repositorio.

## 1. Preparar variables de entorno
Copia `.env.example` y crea `.env`.

Windows PowerShell:
```powershell
Copy-Item .env.example .env
```

Git Bash / macOS / Linux:
```bash
cp .env.example .env
```

Abre `.env` y cambia las contraseñas de ejemplo. No publiques `.env`.

## 2. Construir y levantar los contenedores
```bash
docker compose up --build -d
```

Ver el estado:
```bash
docker compose ps
```

Ver registros:
```bash
docker compose logs -f
```

## 3. Probar la aplicación y la comunicación real
Abre http://localhost:5000 para comprobar que Flask responde.

Guardar un dato (PowerShell):
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5000/mensajes -ContentType "application/json" -Body '{"mensaje":"Hola desde Docker"}'
```

Guardar un dato (Git Bash / macOS / Linux):
```bash
curl -X POST http://localhost:5000/mensajes \
  -H "Content-Type: application/json" \
  -d '{"mensaje":"Hola desde Docker"}'
```

Leer los datos guardados:
```bash
curl http://localhost:5000/mensajes
```

En PowerShell también puedes usar:
```powershell
Invoke-RestMethod http://localhost:5000/mensajes
```

La aplicación se conecta a MySQL usando `DB_HOST=db`. `db` es el nombre del servicio en Docker Compose; no se usa `localhost` ni una IP fija entre contenedores.

## 4. Evidencias de Docker
```bash
docker build -t proyecto-docker-app:manual ./app
docker compose up --build -d
docker ps
docker network inspect proyecto-docker_red-proyecto
```

El nombre real de la red también se puede consultar con:
```bash
docker network ls
```

Para consultar registros:
```bash
docker compose logs app
docker compose logs db
```

## 5. Detener el proyecto
```bash
docker compose down
```

Para borrar también los datos guardados en el volumen (acción irreversible):
```bash
docker compose down -v
```

## 6. Publicar en GitHub
```bash
git init -b main
git add .
git commit -m "Crea aplicación Flask y servicio MySQL con Docker"
git remote add origin https://github.com/USUARIO/NOMBRE-REPOSITORIO.git
git push -u origin main
```

Antes de publicar, confirma que `.env` no está incluido:
```bash
git status
```

## Arquitectura
El navegador accede a Flask por el puerto 5000. Flask se comunica con MySQL por la red privada `red-proyecto`, usando el nombre DNS `db` y el puerto interno 3306. MySQL conserva sus datos en el volumen `datos_mysql`.

## CI
GitHub Actions valida el archivo Compose y construye las imágenes `app` y `db` en cada push o pull request hacia `main`.
