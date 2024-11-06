from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
 
usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

cliente = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.vhjwo.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

try:
   cliente.admin.command('ping')
   print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
   print(e)

baseDatos = cliente["mi_primera_base_datos"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = { "nombre": "Domi", "apellido": "Delgado" }

insercion = coleccion.insert_one(documento)

print(insercion)


