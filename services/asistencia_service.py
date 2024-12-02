from utils.db_connector import get_db_connection
from datetime import datetime

def registrar_asistencia(id_empleado, tipo_evento, comentario=None):
    """
    Registra un evento de asistencia en la base de datos.
    Verifica si ya existe un registro del mismo tipo para el empleado en el día actual.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        
        # Verificar si ya existe un registro del mismo tipo hoy
        query_verificacion = """
            SELECT COUNT(*) FROM registros_asistencia 
            WHERE id_empleado = %s 
            AND tipo_evento = %s 
            AND DATE(fecha_hora) = CURRENT_DATE
        """
        cursor.execute(query_verificacion, (id_empleado, tipo_evento))
        cantidad = cursor.fetchone()[0]
        
        if cantidad > 0:
            return {
                'success': False, 
                'message': 'Ya existe un registro de este tipo para el día de hoy'
            }

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
