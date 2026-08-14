from app import create_app

# This is what Render looks for
application = create_app()

if __name__ == "__main__":
    application.run()