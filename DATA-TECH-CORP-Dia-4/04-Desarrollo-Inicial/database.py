import sqlite3

NOMBRE_BASE_DATOS = "data_tech_corp.db"

def obtener_conexion():
    conexion = sqlite3.connect(NOMBRE_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_base_de_datos():
    conexion = obtener_conexion()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS Solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            prioridad TEXT NOT NULL CHECK (prioridad IN ('baja', 'media', 'alta')),
            estado TEXT NOT NULL DEFAULT 'pendiente'
                CHECK (estado IN ('pendiente', 'en progreso', 'completada'))
        )
    """)
    conexion.commit()
    conexion.close()

def guardar_solicitud(titulo, descripcion, prioridad):
    conexion = obtener_conexion()
    conexion.execute(
        "INSERT INTO Solicitudes (titulo, descripcion, prioridad) VALUES (?, ?, ?)",
        (titulo, descripcion, prioridad)
    )
    conexion.commit()
    conexion.close()

def obtener_solicitudes():
    conexion = obtener_conexion()
    datos = conexion.execute(
        "SELECT id, titulo, descripcion, prioridad, estado FROM Solicitudes ORDER BY id DESC"
    ).fetchall()
    conexion.close()
    return datos
