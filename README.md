📅 CRUD de Gestión de Citas Médicas
Este es un sistema de gestión de citas médicas que permite crear, leer, actualizar y eliminar (CRUD) registros de pacientes y citas. Inicialmente, se desarrolló utilizando MongoDB como base de datos NoSQL, pero luego se migró a MySQL para una integración más estructurada con HeidiSQL.


![image](https://github.com/user-attachments/assets/b426bdb9-6046-4385-9e89-7302657517cc)
![image](https://github.com/user-attachments/assets/15de9386-d331-4946-88e6-40d057a59273)


🚀 Características del Proyecto
✅ Registrar nuevas citas médicas.
✅ Editar la información de las citas.
✅ Eliminar citas de la base de datos.
✅ Listar todas las citas almacenadas.
✅ Interfaz web responsiva con Bootstrap.
✅ Conexión a MySQL (HeidiSQL) y soporte opcional para MongoDB.

🛠️ Tecnologías Utilizadas
🔹 Backend: Python (Flask)
🔹 Base de datos: MySQL (HeidiSQL) & MongoDB (opcional)
🔹 Frontend: HTML, CSS, JavaScript, Bootstrap
🔹 ORM: MySQL Connector (para consultas en MySQL)
🔹 MongoDB: PyMongo (opcional)

📁 Estructura del Proyecto
bash
Copiar
Editar
📂 CRUD_Gestion_Citas/
│── 📂 static/                # Archivos CSS y JS
│── 📂 templates/             # Archivos HTML (interfaz de usuario)
│── 📜 app.py                 # Archivo principal (Flask)
│── 📜 database.py            # Conexión a MySQL/MongoDB
│── 📜 citas.py               # Modelo de datos para citas
│── 📜 requirements.txt       # Librerías necesarias
│── 📜 README.md              # Este archivo
🔌 Instalación y Configuración
📝 1. Clonar el repositorio
sh
Copiar
Editar
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
🛠️ 2. Crear y activar el entorno virtual
sh
Copiar
Editar
# En Windows
python -m venv .venv
.venv\Scripts\activate

# En macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
📦 3. Instalar dependencias
sh
Copiar
Editar
pip install -r requirements.txt
🎯 Configuración de la Base de Datos
🔹 Conexión con MySQL (HeidiSQL)
Abre HeidiSQL y crea una base de datos llamada db_citas_medicas.

En database.py, configura los datos de conexión:

python
Copiar
Editar
import mysql.connector

def dbConnection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="db_citas_medicas"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
Ejecuta el siguiente script SQL en HeidiSQL para crear la tabla:

sql
Copiar
Editar
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    document VARCHAR(50) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    direction VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    doctor VARCHAR(100) NOT NULL
);
🔹 Conexión opcional con MongoDB
Si prefieres usar MongoDB en lugar de MySQL, sigue estos pasos:

Instala MongoDB en tu computadora o usa MongoDB Atlas.

En database.py, usa esta configuración:

python
Copiar
Editar
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://tu_usuario:tu_contraseña@cluster.mongodb.net/db_citas_medicas"

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["db_citas_medicas"]
        return db
    except Exception as e:
        print(f"Error de conexión con MongoDB: {e}")
        return None
Ejecuta el servidor de MongoDB antes de iniciar la app.

▶️ Ejecutar la Aplicación
Una vez configurada la base de datos, ejecuta el servidor Flask:

sh
Copiar
Editar
python app.py
Luego abre tu navegador y ve a:
🔗 http://127.0.0.1:5000/

📌 Diferencias entre MySQL y MongoDB en este Proyecto
Característica	MySQL (HeidiSQL)	MongoDB
Tipo de base de datos	Relacional (SQL)	NoSQL (Documentos)
Estructura de datos	Tablas y filas	Documentos JSON
Integridad referencial	Sí (Claves primarias y foráneas)	No (Datos no estructurados)
Flexibilidad	Más rígido, requiere esquema definido	Más flexible, permite datos dinámicos
Consulta de datos	SQL (SELECT, INSERT, UPDATE)	BSON (find, insert, update)
Rendimiento	Mejor para transacciones complejas	Mejor para grandes volúmenes de datos
📌 ¿Cuál elegir?
Usa MySQL si necesitas estructura y relaciones claras entre datos.

Usa MongoDB si necesitas flexibilidad y escalabilidad.

🔄 Migración de MongoDB a MySQL
Si ya tienes datos en MongoDB y quieres migrarlos a MySQL, puedes hacerlo con un script en Python:

python
Copiar
Editar
import mysql.connector
from pymongo import MongoClient

# Conexión a MongoDB
mongo_client = MongoClient("mongodb+srv://tu_usuario:tu_contraseña@cluster.mongodb.net/db_citas_medicas")
mongo_db = mongo_client["db_citas_medicas"]
mongo_citas = mongo_db["citas"]

# Conexión a MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="db_citas_medicas"
)
mysql_cursor = mysql_conn.cursor()

# Migrar datos
for cita in mongo_citas.find():
    mysql_cursor.execute("""
        INSERT INTO citas (name, document, phone, direction, date, doctor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (cita["name"], cita["document"], cita["phone"], cita["direction"], cita["date"], cita["doctor"]))

mysql_conn.commit()
mysql_cursor.close()
mysql_conn.close()
Este script copia los datos de MongoDB a MySQL automáticamente.

📄 Licencia
Este proyecto está bajo la licencia MIT, lo que significa que puedes modificarlo y distribuirlo libremente.

📞 Contacto: Kilo Kilito Kilogramo Kilovatio 3163898004
Si tienes dudas o sugerencias, puedes contactarme en:
📧 kevindavidtabares.123@gmail.com
🔗 GitHub

