from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from flask_sqlalchemy  import SQLAlchemy
from flask_mail import Mail, Message

# Globally accessible libraries
db = SQLAlchemy()
SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = "secret key"
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'ndhp.gov@gmail.com'
    app.config['MAIL_PASSWORD'] = '1234Test@'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        db.create_all()

        import blueprint
        app.register_blueprint(blueprint.main_bp)
        return app