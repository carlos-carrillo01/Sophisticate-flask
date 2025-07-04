import os
from dotenv import load_dotenv  # Opcional, pero recomendado para variables sensibles

# Cargar variables de entorno desde .env (opcional)
load_dotenv()

class Config:
    # Configuración básica
    SECRET_KEY = os.getenv('SECRET_KEY', 'una-clave-secreta-muy-segura-aqui')
    DEBUG = False
    TESTING = False
    
    # Configuración de Flask
    TEMPLATES_AUTO_RELOAD = True
    
    # Configuración de archivos estáticos
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    # Puedes añadir configuraciones específicas para tu diseño
    SITE_NAME = "Sophisticate"
    SITE_DESCRIPTION = "Soluciones Digitales Modernas"
    CONTACT_EMAIL = "info@sophisticate.com"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'clave-de-desarrollo'  # En producción usa una variable de entorno

class TestingConfig(Config):
    TESTING = True