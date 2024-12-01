from flask import Flask, request, jsonify, render_template, redirect
from services.auth_service import verify_token
from services.asistencia_service import registrar_asistencia
from services.permisos_service import solicitar_permiso

app = Flask(__name__)

BASE_PHP_URL = "http://localhost/sistema-asistencia/"  # Cambiar según el entorno

@app.route('/asistencia', methods=['GET'])
def asistencia():
    token = request.args.get('token')
    if not token:
        return jsonify({'success': False, 'message': 'Token no proporcionado'}), 400

    session = verify_token(token)
    if session and session['id_rol'] == 2:
        return render_template('asistencia.html', empleado_id=session['id_empleado'], token=token)
    else:
        return jsonify({'success': False, 'message': 'Acceso denegado o token inválido'}), 403

@app.route('/asistencia_registro', methods=['POST'])
def asistencia_registro():
    token = request.args.get('token')
    tipo_evento = request.args.get('tipo_evento')
    comentario = request.form.get('comentario', None)

    if not token or not tipo_evento:
        return jsonify({'success': False, 'message': 'Token o tipo de evento no proporcionado'}), 400

    session = verify_token(token)
    if session and session['id_rol'] == 2:
        result = registrar_asistencia(session['id_empleado'], tipo_evento, comentario)
        return jsonify(result)
    else:
        return jsonify({'success': False, 'message': 'Acceso denegado o token inválido'}), 403

@app.route('/permisos', methods=['GET'])
def permisos():
    token = request.args.get('token')
    if not token:
        return jsonify({'success': False, 'message': 'Token no proporcionado'}), 400

    session = verify_token(token)
    if session and session['id_rol'] == 2:
        return render_template('permisos.html', empleado_id=session['id_empleado'], token=token)
    else:
        return jsonify({'success': False, 'message': 'Acceso denegado o token inválido'}), 403

@app.route('/permisos_solicitud', methods=['POST'])
def permisos_solicitud():
    token = request.args.get('token')
    tipo_permiso = request.form.get('tipo_permiso')
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_fin = request.form.get('fecha_fin')

    if not token or not tipo_permiso or not fecha_inicio or not fecha_fin:
        return jsonify({'success': False, 'message': 'Faltan datos para procesar la solicitud'}), 400

    session = verify_token(token)
    if session and session['id_rol'] == 2:
        result = solicitar_permiso(session['id_empleado'], tipo_permiso, fecha_inicio, fecha_fin)
        return jsonify(result)
    else:
        return jsonify({'success': False, 'message': 'Acceso denegado o token inválido'}), 403

@app.route('/logout', methods=['GET'])
def logout():
    return redirect(f"{BASE_PHP_URL}logout.php")

if __name__ == '__main__':
    app.run(debug=True)
