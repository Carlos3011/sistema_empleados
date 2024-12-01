# utils/db_connector.py

import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    """
    Establece una conexión con la base de datos usando la configuración proporcionada.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise
