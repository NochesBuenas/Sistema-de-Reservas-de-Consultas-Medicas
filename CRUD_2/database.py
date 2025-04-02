import mysql.connector

def dbConnection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # O la IP del servidor MySQL
            user="root",      # Usuario de MySQL
            password="",  # Contraseña de MySQL
            database="citasmedicas"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión a MySQL: {err}")
        return None
