from flask import Flask
from database import inicializar_base_de_datos

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Data-Tech Corp: aplicación inicial en funcionamiento."

if __name__ == "__main__":
    inicializar_base_de_datos()
    app.run(debug=True)
