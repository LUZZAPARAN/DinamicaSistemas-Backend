from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_db():
    # Leer la URI de conexión desde el archivo .env
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client["DinamicaSistemas"]  # Cambia "event_calendar" por el nombre de tu base de datos
    return db
