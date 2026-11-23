from flask import Flask, render_template, request, redirect, url_for, abort
from database import inicializar_bd, crear_solicitud, obtener_solicitudes, obtener_solicitud, actualizar_estado, obtener_resumen

app = Flask(__name__)
inicializar_bd()

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        prioridad = request.form.get("prioridad", "media")
        if titulo and descripcion:
            crear_solicitud(titulo, descripcion, prioridad)
        return redirect(url_for("inicio"))

    busqueda = request.args.get("busqueda", "").strip()
    estado = request.args.get("estado", "")
    prioridad = request.args.get("prioridad", "")
    solicitudes = obtener_solicitudes(busqueda, estado, prioridad)
    resumen = obtener_resumen()
    return render_template("index.html", solicitudes=solicitudes, resumen=resumen,
                           busqueda=busqueda, estado=estado, prioridad=prioridad)

@app.route("/solicitud/<int:solicitud_id>", methods=["GET", "POST"])
def detalle(solicitud_id):
    solicitud = obtener_solicitud(solicitud_id)
    if solicitud is None:
        abort(404)
    if request.method == "POST":
        nuevo_estado = request.form.get("estado", "pendiente")
        if nuevo_estado in ("pendiente", "en progreso", "completada"):
            actualizar_estado(solicitud_id, nuevo_estado)
        return redirect(url_for("detalle", solicitud_id=solicitud_id))
    return render_template("detalle.html", solicitud=solicitud)

if __name__ == "__main__":
    app.run(debug=True)
