# Día 4 – Desarrollo inicial

## Objetivo
Crear una primera versión funcional para registrar y consultar solicitudes de soporte técnico.

## Archivos
- `app.py`: rutas de Flask y formulario.
- `database.py`: creación y manejo de la tabla de solicitudes.
- `templates/index.html`: página principal.
- `static/css/estilos.css`: estilos visuales.
- `Avance_del_Desarrollo_Dia_4.docx`: explicación del trabajo.
- `Registro_de_Horas_Dia_4.docx`: planificación estimada.

## Cómo ejecutar
1. Abrir una terminal dentro de esta carpeta.
2. Crear un entorno virtual: `python -m venv .venv`.
3. Activarlo en Windows: `.venv\\Scripts\\activate`.
4. Instalar Flask: `pip install -r requirements.txt`.
5. Ejecutar `python app.py` (o `py app.py`).
6. Abrir `http://127.0.0.1:5000` en el navegador.
7. Registrar una solicitud de prueba con información ficticia y verificar que aparezca en la lista.

La base de datos SQLite se crea al iniciar la aplicación. No subir el entorno virtual ni la base de datos generada. Usar únicamente datos ficticios.
