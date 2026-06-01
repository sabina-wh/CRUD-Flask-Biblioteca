from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    # Configuración
    from .config import Config
    app.config.from_object(Config)

    # Base de datos
    db.init_app(app)

    # CSRF
    csrf.init_app(app) 

    # Importar modelos
    from . import models

    # Registrar rutas
    from .routes import registrar_rutas
    registrar_rutas(app)

    return app
