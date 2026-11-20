from flask import Flask, render_template, request, redirect, url_for, flash
from database import inicializar_base_de_datos, guardar_solicitud, obtener_solicitudes

app = Flask(__name__)
app.secret_key = "clave-local-para-pruebas"

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        prioridad = request.form.get("prioridad", "media")
        if not titulo or not descripcion:
            flash("Complete el título y la descripción.")
            return redirect(url_for("inicio"))
        if prioridad not in ("baja", "media", "alta"):
            prioridad = "media"
        guardar_solicitud(titulo, descripcion, prioridad)
        flash("La solicitud se registró correctamente.")
        return redirect(url_for("inicio"))
    return render_template("index.html", solicitudes=obtener_solicitudes())

if __name__ == "__main__":
    inicializar_base_de_datos()
    app.run(debug=True)
