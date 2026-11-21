from flask import Flask, render_template, request, redirect, url_for, abort
from database import inicializar_base_datos, obtener_solicitudes, obtener_solicitud, actualizar_estado

app = Flask(__name__)
inicializar_base_datos()

@app.route("/")
def inicio():
    return render_template("index.html", solicitudes=obtener_solicitudes())

@app.route("/solicitud/<int:solicitud_id>")
def detalle_solicitud(solicitud_id):
    solicitud = obtener_solicitud(solicitud_id)
    if solicitud is None:
        abort(404)
    return render_template("detalle.html", solicitud=solicitud)

@app.route("/solicitud/<int:solicitud_id>/actualizar", methods=["POST"])
def actualizar_solicitud(solicitud_id):
    if obtener_solicitud(solicitud_id) is None:
        abort(404)
    nuevo_estado = request.form.get("estado", "")
    if nuevo_estado in ["pendiente", "en progreso", "completada"]:
        actualizar_estado(solicitud_id, nuevo_estado)
    return redirect(url_for("detalle_solicitud", solicitud_id=solicitud_id))

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "No se encontró la solicitud solicitada.", 404

if __name__ == "__main__":
    app.run(debug=True)
