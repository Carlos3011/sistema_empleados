from utils.db_connector import get_db_connection

def solicitar_permiso(id_empleado, tipo_permiso, fecha_inicio, fecha_fin):
    """
    Registra una solicitud de permiso en la base de datos.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO permisos (id_empleado, tipo_permiso, fecha_inicio, fecha_fin, estado)
            VALUES (%s, %s, %s, %s, 'pendiente')
        """
        cursor.execute(query, (id_empleado, tipo_permiso, fecha_inicio, fecha_fin))
        connection.commit()
        return {'success': True, 'message': 'Permiso solicitado correctamente'}
    except Exception as e:
        print(f"Error al solicitar permiso: {e}")
        return {'success': False, 'message': 'Error al solicitar permiso'}
    finally:
        cursor.close()
        connection.close()
