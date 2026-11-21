import sqlite3

NOMBRE_BASE_DATOS = "solicitudes.db"

def conectar():
    conexion = sqlite3.connect(NOMBRE_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_base_datos():
    conexion = conectar()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'pendiente'
        )
    """)
    cantidad = conexion.execute("SELECT COUNT(*) FROM solicitudes").fetchone()[0]
    if cantidad == 0:
        ejemplos = [
            ("Computadora no enciende", "El equipo no inicia.", "alta", "pendiente"),
            ("Problema con impresora", "La impresora no responde.", "media", "en progreso"),
            ("Instalación de programa", "Se necesita instalar un programa autorizado.", "baja", "completada")
        ]
        conexion.executemany(
            "INSERT INTO solicitudes (titulo, descripcion, prioridad, estado) VALUES (?, ?, ?, ?)",
            ejemplos
        )
    conexion.commit()
    conexion.close()

def obtener_solicitudes():
    conexion = conectar()
    datos = conexion.execute("SELECT * FROM solicitudes ORDER BY id DESC").fetchall()
    conexion.close()
    return datos

def obtener_solicitud(solicitud_id):
    conexion = conectar()
    dato = conexion.execute("SELECT * FROM solicitudes WHERE id = ?", (solicitud_id,)).fetchone()
    conexion.close()
    return dato

def actualizar_estado(solicitud_id, nuevo_estado):
    conexion = conectar()
    conexion.execute("UPDATE solicitudes SET estado = ? WHERE id = ?", (nuevo_estado, solicitud_id))
    conexion.commit()
    conexion.close()
