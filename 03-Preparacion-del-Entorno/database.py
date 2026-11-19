import sqlite3

NOMBRE_BASE_DATOS = "data_tech_corp.db"

def obtener_conexion():
    conexion = sqlite3.connect(NOMBRE_BASE_DATOS)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_base_de_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            rol TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            prioridad TEXT NOT NULL
                CHECK (prioridad IN ('baja', 'media', 'alta')),
            estado TEXT NOT NULL DEFAULT 'pendiente'
                CHECK (estado IN ('pendiente', 'en progreso', 'completada')),
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
        )
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    inicializar_base_de_datos()
    print("Base de datos creada o verificada correctamente.")
