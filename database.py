from pymongo import MongoClient 
import certifi  

MONGO_URI = 'mongodb+srv://kevindavidtabares123:Callese123@cluster1.ky2wm.mongodb.net/'
ca = certifi.where()

def dbConnecction():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_citas_medicas"]
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db
