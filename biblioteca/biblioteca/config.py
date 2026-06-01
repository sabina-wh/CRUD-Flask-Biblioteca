import os

BASE_DIR = os.path.dirname(__file__)
DB_FILE_PATH = os.path.join(BASE_DIR, "biblioteca.db")

class Config:
    SECRET_KEY = 'mi-clave-secreta'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'portadas')# Carpeta donde se guardarán las imágenes