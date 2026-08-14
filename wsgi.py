from app import create_app

# Render looks for a variable named 'application' or 'app'
application = create_app()

if __name__ == "__main__":
    application.run()