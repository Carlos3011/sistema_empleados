from flask import Flask, render_template
from controllers.empleados_controller import empleados_bp

app = Flask(__name__)
app.secret_key = "secret_key"  # Cambiar a una clave más segura

# Registrar el Blueprint de empleados
app.register_blueprint(empleados_bp, url_prefix="/empleados")

@app.route("/")
def index():
    """
    Ruta principal que renderiza la página de inicio.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
