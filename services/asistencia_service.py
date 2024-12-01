from utils.db_connector import get_db_connection
from datetime import datetime

def registrar_asistencia(id_empleado, tipo_evento, comentario=None):
    """
    Registra un evento de asistencia en la base de datos.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO registros_asistencia (id_empleado, tipo_evento, fecha_hora, comentario)
            VALUES (%s, %s, %s, %s)
        """
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (id_empleado, tipo_evento, fecha_hora, comentario))
        connection.commit()
        return {'success': True, 'message': 'Asistencia registrada correctamente'}
    except Exception as e:
        print(f"Error al registrar asistencia: {e}")
        return {'success': False, 'message': 'Error al registrar asistencia'}
    finally:
        cursor.close()
        connection.close()
