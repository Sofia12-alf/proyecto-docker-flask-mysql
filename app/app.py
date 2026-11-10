git config --global user.name "Tu Nombre"import os
import time
from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
    )

def preparar_base_datos():
    # Espera a que MySQL termine de iniciar.
    for intento in range(30):
        conexion = None
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mensajes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    mensaje VARCHAR(255) NOT NULL,
                    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Base de datos lista.")
            return
        except Error as error:
            print(f"MySQL aún no está listo (intento {intento + 1}/30): {error}")
            if conexion is not None and conexion.is_connected():
                conexion.close()
            time.sleep(2)
    raise RuntimeError("No fue posible conectar con MySQL después de varios intentos.")

@app.get("/")
def inicio():
    return jsonify({
        "estado": "ok",
        "aplicacion": "Flask",
        "mensaje": "Aplicación conectada. Usa POST /mensajes para guardar y GET /mensajes para leer."
    })

@app.post("/mensajes")
def guardar_mensaje():
    datos = request.get_json(silent=True) or request.form
    mensaje = str(datos.get("mensaje", "")).strip()

    if not mensaje:
        return jsonify({"error": "Debes enviar un campo 'mensaje'."}), 400

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO mensajes (mensaje) VALUES (%s)", (mensaje,))
    conexion.commit()
    nuevo_id = cursor.lastrowid
    cursor.close()
    conexion.close()

    return jsonify({"resultado": "guardado", "id": nuevo_id, "mensaje": mensaje}), 201

@app.get("/mensajes")
def listar_mensajes():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, mensaje, creado_en
        FROM mensajes
        ORDER BY id DESC
        LIMIT 50
    """)
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()

    for fila in filas:
        fila["creado_en"] = fila["creado_en"].isoformat(sep=" ")
    return jsonify(filas)

if __name__ == "__main__":
    preparar_base_datos()
    app.run(host="0.0.0.0", port=5000)
