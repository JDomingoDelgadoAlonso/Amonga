from pymongo import MongoClient
from dotenv import load_dotenv
import os

class ConectorMongoDB():
    def conectarse(self):
        load_dotenv()

        usuario = os.getenv("USUARIO_MONGODB")
        password = os.getenv("PASSWORD_MONGODB")
        cluster = os.getenv("CLUSTER_MONGODB")

        uri = f"mongodb+srv://{usuario}:{password}@{cluster}.vhjwo.mongodb.net/?retryWrites=true&w=majority&appName={cluster}"

        cliente = MongoClient(uri, maxPoolSize=50)
        
        # Test de conexión
        try:
            cliente.admin.command('ping')
            print("Conexión exitosa a MongoDB Atlas!")
        except Exception as e:
            print(f"Error al conectar con MongoDB: {e}")
        
        return cliente
