from flask import Flask
from config import Config
from extensions import db  # Import db from our new extensions file

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database with app
    db.init_app(app)

    # Import models and routes
    from models import Project, Skill, Experience
    from routes.main import main_bp
    
    # Register Blueprints
    app.register_blueprint(main_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)