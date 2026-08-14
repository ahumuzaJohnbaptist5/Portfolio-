import os
from flask import Flask
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Import and register routes
    from routes.main import main_bp
    app.register_blueprint(main_bp)
    
    # Import models (needed for db.create_all)
    from models import Project, Skill, Experience, ContactMessage
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)