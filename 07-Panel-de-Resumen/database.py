import sqlite3

DB_NAME = "solicitudes.db"

def conectar():
    conexion = sqlite3.connect(DB_NAME)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_bd():
    with conectar() as conexion:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS solicitudes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                prioridad TEXT NOT NULL,
                estado TEXT NOT NULL DEFAULT 'pendiente'
            )
        """)

def crear_solicitud(titulo, descripcion, prioridad):
    with conectar() as conexion:
        conexion.execute(
            "INSERT INTO solicitudes (titulo, descripcion, prioridad) VALUES (?, ?, ?)",
            (titulo, descripcion, prioridad)
        )

def obtener_solicitudes(busqueda="", estado="", prioridad=""):
    consulta = "SELECT * FROM solicitudes WHERE titulo LIKE ?"
    parametros = [f"%{busqueda}%"]
    if estado:
        consulta += " AND estado = ?"
        parametros.append(estado)
    if prioridad:
        consulta += " AND prioridad = ?"
        parametros.append(prioridad)
    consulta += " ORDER BY id DESC"
    with conectar() as conexion:
        return conexion.execute(consulta, parametros).fetchall()

def obtener_solicitud(solicitud_id):
    with conectar() as conexion:
        return conexion.execute(
            "SELECT * FROM solicitudes WHERE id = ?", (solicitud_id,)
        ).fetchone()

def actualizar_estado(solicitud_id, estado):
    with conectar() as conexion:
        conexion.execute(
            "UPDATE solicitudes SET estado = ? WHERE id = ?",
            (estado, solicitud_id)
        )

def obtener_resumen():
    with conectar() as conexion:
        total = conexion.execute("SELECT COUNT(*) FROM solicitudes").fetchone()[0]
        pendientes = conexion.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE estado = 'pendiente'"
        ).fetchone()[0]
        progreso = conexion.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE estado = 'en progreso'"
        ).fetchone()[0]
        completadas = conexion.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE estado = 'completada'"
        ).fetchone()[0]
        prioridad_alta = conexion.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE prioridad = 'alta'"
        ).fetchone()[0]
    return {
        "total": total,
        "pendientes": pendientes,
        "progreso": progreso,
        "completadas": completadas,
        "prioridad_alta": prioridad_alta
    }
