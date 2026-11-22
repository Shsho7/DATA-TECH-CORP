# Día 6 - Búsqueda y filtros de solicitudes

## Objetivo
Añadir opciones para buscar solicitudes por título y filtrarlas por estado y prioridad.

## Funciones incluidas
- Buscar solicitudes por parte del título.
- Filtrar por estado: pendiente, en progreso o completada.
- Filtrar por prioridad: baja, media o alta.
- Combinar los criterios de búsqueda.
- Limpiar los filtros y volver a mostrar todas las solicitudes.
- Mantener el registro, los detalles y la actualización de estado.

## Archivos
- `app.py`: rutas y funcionamiento principal de Flask.
- `database.py`: conexión y consultas a SQLite.
- `templates/`: páginas del sistema.
- `static/css/estilos.css`: estilos visuales.
- `requirements.txt`: dependencia necesaria.
- `.gitignore`: archivos excluidos de GitHub.

## Cómo ejecutar
1. Abrir esta carpeta en la computadora.
2. Instalar la dependencia con `pip install -r requirements.txt`.
3. Ejecutar `python app.py`.
4. Abrir en el navegador la dirección local que muestra Flask.

La base de datos `solicitudes.db` se crea automáticamente al iniciar.

## Nota
Esta versión es para práctica académica local. Un sistema de producción requiere medidas adicionales de seguridad.
