from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
lm = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = 'your_secret_key' # Replace with strong secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #SQLite for development
    app.config['MAIL_SERVER'] = 'smtp.example.com' # TODO: Mail server
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'username' # TODO: Mail username
    app.config['MAIL_PASSWORD'] = 'password' # TODO: Mail password

    # Initialize extensions
    db.init_app(app)
    lm.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from app.routes import routes
    app.register_blueprint(routes)

    return app