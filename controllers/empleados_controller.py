from flask import Blueprint, render_template, request, jsonify, flash
from models.empleados_model import obtener_empleados_activos, registrar_asistencia, solicitar_permiso

# Crear un Blueprint para los empleados
empleados_bp = Blueprint("empleados", __name__)

@empleados_bp.route("/lista", methods=["GET", "POST"])
def lista():
    """
    Ruta para gestionar la lista de empleados y registrar eventos de asistencia.
    """
    if request.method == "POST":
        id_empleado = request.form["id_empleado"]
        tipo_evento = request.form["tipo_evento"]
        comentario = request.form.get("comentario", None)
        registrar_asistencia(id_empleado, tipo_evento, comentario)
        return jsonify({"message": "Evento registrado exitosamente"})
    empleados = obtener_empleados_activos()
    return render_template("empleados_lista.html", empleados=empleados)

@empleados_bp.route("/permisos", methods=["GET", "POST"])
def permisos():
    """
    Ruta para gestionar las solicitudes de permisos de empleados.
    """
    if request.method == "POST":
        id_empleado = request.form["id_empleado"]
        tipo_permiso = request.form["tipo_permiso"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        solicitar_permiso(id_empleado, tipo_permiso, fecha_inicio, fecha_fin)
        return jsonify({"message": "Permiso solicitado exitosamente"})
    empleados = obtener_empleados_activos()
    return render_template("empleados_permisos.html", empleados=empleados)
