import pymongo
from bson import ObjectId

HOST = "127.0.0.1"
PORT = "27017"
DATABASE = 'capacitacion'
COLLECTION = 'usuarios'
URI_CONEXION = "mongodb://" + HOST + ":" + PORT + "/"

def consultar():
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {}
        resultado = coleccion.find(condicion)
        data = resultado
    except Exception as error:
        print("Error consultando datos", error)

    finally:
        return data

def insertar(data):
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        coleccion = cliente[DATABASE][COLLECTION]
        coleccion.insert_one(data)
        print("data insertada")
    except Exception as error:
        print("Error insertando datos", error)

def eliminar_porid(id):
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        coleccion.delete_one(condicion)
        
    except Exception as error:
        print("Error borrando datos", error)

def consultar_porid(id):
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id':ObjectId(id)}
        resultado = coleccion.find_one(condicion)
        data = resultado
    except Exception as error:
        print("Error consultando datos", error)

    finally:
        return data

def actualizar(id, data):
    try:
        cliente = pymongo.MongoClient(URI_CONEXION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        valores = {'$set': data}
        coleccion.update_one(condicion, valores)
        
    except Exception as error:
        print("Error actualizando datos", error)

if __name__ == '__main__':
    
    data = consultar()
    for k in data:
        print(k)
