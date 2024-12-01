import mysql.connector

# Configuración de conexión a la base de datos
DB_CONFIG = {
    'host': 'localhost',  # Dirección del servidor MySQL
    'user': 'root',             # Usuario de la base de datos
    'password': '',      # Contraseña de la base de datos
    'database': 'sistema_asistencia', # Nombre de la base de datos
    'port': 3306                      # Puerto de MySQL (por defecto: 3306)
}

def execute_query(query, params=()):
    """
    Ejecuta una consulta SQL en la base de datos.
    :param query: La consulta SQL que se ejecutará.
    :param params: Una tupla con los parámetros para la consulta.
    :return: Los resultados de la consulta, si los hay.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)  # Devuelve los resultados como diccionarios
        cursor.execute(query, params)
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()  # Obtiene los datos para consultas SELECT
        else:
            conn.commit()  # Guarda cambios para INSERT/UPDATE/DELETE
            results = None
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as e:
        print(f"Error en la base de datos: {e}")
        return None

# Funciones específicas del modelo
def obtener_empleados_activos():
    """
    Obtiene todos los empleados activos.
    :return: Lista de empleados activos.
    """
    query = "SELECT id_empleado, nombre, apellido FROM empleados WHERE activo = 1"
    return execute_query(query)

def registrar_asistencia(id_empleado, tipo_evento, comentario=None):
    """
    Registra un evento de asistencia en la base de datos.
    :param id_empleado: ID del empleado.
    :param tipo_evento: Tipo de evento ('entrada', 'salida_a_comer', etc.).
    :param comentario: Comentarios adicionales (opcional).
    """
    query = """
        INSERT INTO registros_asistencia (id_empleado, tipo_evento, fecha_hora, comentario)
        VALUES (%s, %s, NOW(), %s)
    """
    execute_query(query, (id_empleado, tipo_evento, comentario))

def solicitar_permiso(id_empleado, tipo_permiso, fecha_inicio, fecha_fin):
    """
    Solicita un permiso para un empleado.
    :param id_empleado: ID del empleado.
    :param tipo_permiso: Tipo de permiso (e.g., 'vacaciones', 'enfermedad').
    :param fecha_inicio: Fecha y hora de inicio del permiso.
    :param fecha_fin: Fecha y hora de fin del permiso.
    """
    query = """
        INSERT INTO permisos (id_empleado, tipo_permiso, fecha_inicio, fecha_fin, estado)
        VALUES (%s, %s, %s, %s, 'pendiente')
    """
    execute_query(query, (id_empleado, tipo_permiso, fecha_inicio, fecha_fin))
