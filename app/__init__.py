from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

mail = Mail()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
        MAIL_DEFAULT_SENDER=os.getenv("MAIL_USERNAME")
    )

    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
