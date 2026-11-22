from flask import Flask, render_template, request, redirect, url_for, flash
from database import (
    crear_tabla, obtener_solicitudes, obtener_solicitud_por_id,
    agregar_solicitud, actualizar_estado
)

app = Flask(__name__)
app.secret_key = "clave-local-para-practica"
crear_tabla()

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        prioridad = request.form.get("prioridad", "media")
        if not titulo or not descripcion:
            flash("Complete el título y la descripción.")
            return redirect(url_for("inicio"))
        if prioridad not in ["baja", "media", "alta"]:
            prioridad = "media"
        agregar_solicitud(titulo, descripcion, prioridad)
        flash("La solicitud se registró correctamente.")
        return redirect(url_for("inicio"))

    estado = request.args.get("estado", "")
    prioridad = request.args.get("prioridad", "")
    busqueda = request.args.get("busqueda", "").strip()
    if estado not in ["", "pendiente", "en progreso", "completada"]:
        estado = ""
    if prioridad not in ["", "baja", "media", "alta"]:
        prioridad = ""
    solicitudes = obtener_solicitudes(estado, prioridad, busqueda)
    return render_template(
        "index.html", solicitudes=solicitudes, estado=estado,
        prioridad=prioridad, busqueda=busqueda
    )

@app.route("/solicitud/<int:solicitud_id>")
def detalle(solicitud_id):
    solicitud = obtener_solicitud_por_id(solicitud_id)
    if solicitud is None:
        return "Solicitud no encontrada", 404
    return render_template("detalle.html", solicitud=solicitud)

@app.route("/actualizar/<int:solicitud_id>", methods=["POST"])
def actualizar(solicitud_id):
    estado = request.form.get("estado", "")
    if estado not in ["pendiente", "en progreso", "completada"]:
        flash("El estado seleccionado no es válido.")
        return redirect(url_for("detalle", solicitud_id=solicitud_id))
    if obtener_solicitud_por_id(solicitud_id) is None:
        return "Solicitud no encontrada", 404
    actualizar_estado(solicitud_id, estado)
    flash("El estado se actualizó correctamente.")
    return redirect(url_for("detalle", solicitud_id=solicitud_id))

if __name__ == "__main__":
    app.run(debug=True)
