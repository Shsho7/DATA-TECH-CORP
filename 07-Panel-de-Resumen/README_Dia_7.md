# Día 7 – Panel de resumen

## Objetivo
Añadir un panel con el total de solicitudes, las solicitudes pendientes, en progreso, completadas y las de prioridad alta.

## Archivos
- `app.py`: rutas principales de la aplicación Flask.
- `database.py`: creación de la tabla y operaciones con SQLite, incluidos los conteos del panel.
- `templates/index.html`: formulario, panel, búsqueda, filtros y lista de solicitudes.
- `templates/detalle.html`: detalle y actualización del estado.
- `static/css/estilos.css`: estilos básicos.
- `Panel_de_Resumen_Dia_7.docx`: descripción del trabajo y registro de horas.

## Cómo ejecutar
1. Abrir una terminal dentro de esta carpeta.
2. Crear un entorno virtual: `python -m venv venv`.
3. Activarlo según el sistema operativo.
4. Instalar Flask: `pip install -r requirements.txt`.
5. Ejecutar: `python app.py`.
6. Abrir en el navegador la dirección local que muestra Flask.

La base de datos `solicitudes.db` se crea automáticamente al iniciar la aplicación.

## Nota
Este día continúa el prototipo de los días anteriores. Antes de reemplazar archivos del proyecto en GitHub, conservar una copia de la versión anterior.
