# Informe de evidencias – Proyecto Docker

> Completa este documento con capturas reales de tu computador. No entregues los espacios vacíos como si fueran evidencias.

## 1. Objetivo
Implementar una solución de dos contenedores donde una aplicación Flask se comunica con una base de datos MySQL mediante Docker Compose.

## 2. Arquitectura
Usuario/navegador → `app` (Flask, puerto 5000) → red `red-proyecto` → `db` (MySQL, puerto interno 3306) → volumen `datos_mysql`.

## 3. Evidencias requeridas
Inserta una captura real debajo de cada título:

1. **Construcción de imagen:** salida de `docker build -t proyecto-docker-app:manual ./app`.
2. **Docker Compose:** salida de `docker compose up --build -d`.
3. **Contenedores activos:** salida de `docker ps` donde aparezcan `app` y `db`.
4. **Red:** salida de `docker network inspect NOMBRE_REAL_DE_LA_RED`.
5. **Comunicación:** resultado de POST a `/mensajes` y luego GET a `/mensajes` mostrando el dato guardado y leído.
6. **CI:** captura del check verde de GitHub Actions.

## 4. Prueba de comunicación
Explica que Flask usa `DB_HOST=db`, donde `db` es el nombre del servicio definido en `docker-compose.yml`. Describe cómo enviaste un mensaje mediante POST, cómo MySQL lo almacenó y cómo lo recuperaste mediante GET.

## 5. Conclusiones
Escribe con tus palabras qué aprendiste sobre imágenes, contenedores, redes, volúmenes, variables de entorno y comunicación entre servicios.

## 6. Referencias (formato APA)
Docker, Inc. (s. f.). *Docker Compose overview*. Docker Documentation. https://docs.docker.com/compose/

Docker, Inc. (s. f.). *Dockerfile reference*. Docker Documentation. https://docs.docker.com/reference/dockerfile/

Oracle. (s. f.). *MySQL 8.4 Reference Manual*. https://dev.mysql.com/doc/refman/8.4/en/

Pallets. (s. f.). *Flask documentation*. https://flask.palletsprojects.com/
