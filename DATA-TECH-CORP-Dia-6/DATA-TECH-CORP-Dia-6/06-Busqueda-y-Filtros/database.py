import sqlite3

NOMBRE_BD = "solicitudes.db"

def conectar():
    conexion = sqlite3.connect(NOMBRE_BD)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    conexion = conectar()
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'pendiente'
        )
    ''')
    conexion.commit()
    conexion.close()

def obtener_solicitudes(estado="", prioridad="", busqueda=""):
    conexion = conectar()
    consulta = "SELECT * FROM solicitudes WHERE 1=1"
    parametros = []
    if estado:
        consulta += " AND estado = ?"
        parametros.append(estado)
    if prioridad:
        consulta += " AND prioridad = ?"
        parametros.append(prioridad)
    if busqueda:
        consulta += " AND titulo LIKE ?"
        parametros.append("%" + busqueda + "%")
    consulta += " ORDER BY id DESC"
    resultado = conexion.execute(consulta, parametros).fetchall()
    conexion.close()
    return resultado

def obtener_solicitud_por_id(solicitud_id):
    conexion = conectar()
    resultado = conexion.execute(
        "SELECT * FROM solicitudes WHERE id = ?", (solicitud_id,)
    ).fetchone()
    conexion.close()
    return resultado

def agregar_solicitud(titulo, descripcion, prioridad):
    conexion = conectar()
    conexion.execute(
        "INSERT INTO solicitudes (titulo, descripcion, prioridad) VALUES (?, ?, ?)",
        (titulo, descripcion, prioridad)
    )
    conexion.commit()
    conexion.close()

def actualizar_estado(solicitud_id, estado):
    conexion = conectar()
    conexion.execute(
        "UPDATE solicitudes SET estado = ? WHERE id = ?",
        (estado, solicitud_id)
    )
    conexion.commit()
    conexion.close()
