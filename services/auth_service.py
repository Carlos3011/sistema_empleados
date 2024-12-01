from utils.db_connector import get_db_connection

def verify_token(token):
    """
    Verifica si el token existe y pertenece a un usuario con rol de empleado.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT e.id_empleado, e.id_rol
            FROM sesiones s
            INNER JOIN empleados e ON s.id_empleado = e.id_empleado
            WHERE s.auth_token = %s
        """
        cursor.execute(query, (token,))
        session = cursor.fetchone()
        return session
    except Exception as e:
        print(f"Error al verificar el token: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
