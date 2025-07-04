from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuraciones
    app.config.from_pyfile('../config.py')
    
    # Registrar blueprints (si los tienes)
    
    # Importar rutas
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app