# Día 5 – Gestión de solicitudes

## Objetivo
Consultar los detalles de una solicitud y actualizar su estado.

## Archivos
- `app.py`: rutas de Flask.
- `database.py`: operaciones con SQLite.
- `templates/index.html`: lista de solicitudes.
- `templates/detalle.html`: detalles y formulario de actualización.
- `static/css/estilos.css`: estilos.
- `Registro_de_Horas_Dia_5.docx`: registro de horas.

## Cómo ejecutar
1. Abre una terminal dentro de esta carpeta.
2. Instala Flask: `pip install -r requirements.txt`.
3. Ejecuta: `python app.py`.
4. Visita `http://127.0.0.1:5000`.

La base de datos se crea automáticamente. Si está vacía, se agregan tres solicitudes de ejemplo.

## Pruebas
- Abrir la página principal.
- Seleccionar «Ver solicitud».
- Cambiar el estado y guardar.
- Regresar a la lista y confirmar el cambio.
- Probar un número de solicitud inexistente.

Esta es una versión académica para pruebas locales. No incluye inicio de sesión ni asignación de técnicos.
