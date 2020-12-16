from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy  import SQLAlchemy
from flask_mail import Mail, Message
import sqlite3



# Globally accessible libraries
db = SQLAlchemy()
SQLALCHEMY_TRACK_MODIFICATIONS = False

conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE IF NOT EXISTS DR_EVENTS (USER_ID varchar(12) PRIMARY KEY NOT NULL, DR_LAB_ID varchar(12) NOT NULL, DATE TEXT NOT NULL, hosptial varchar(30) not null, desc varchar(100));''')
conn.execute('''CREATE TABLE IF NOT EXISTS doctor( uid varchar(10) PRIMARY KEY,  fname varchar(30) NOT NULL,  lname varchar(30) NOT NULL,  email varchar(30) NOT NULL,  mob varchar(30) NOT NULL,  dob varchar(30) NOT NULL,  gender varchar(30) NOT NULL,  regnum varchar(20) NOT NULL,  Specialization varchar(30) NOT NULL,  add3 varchar(30) NOT NULL,  state varchar(15) NOT NULL,  city varchar(30) NOT NULL,  district varchar(30) NOT NULL,  pin integer NOT NULL,  addr1 varchar(30) NOT NULL,  addr2 varchar(30) NOT NULL ) ''')
conn.execute('''CREATE TABLE IF NOT EXISTS LAB_EVENTS (USER_ID varchar(12) PRIMARY KEY NOT NULL, DR_LAB_ID varchar(12) NOT NULL, DATE TEXT NOT NULL , hosptial varchar(30) not null, desc varchar(100));''')
conn.execute('''CREATE TABLE IF NOT EXISTS "individual" ( "id" TEXT NOT NULL, "pasw" TEXT NOT NULL, "fname" TEXT, "lname" TEXT, "email" TEXT, "mob" TEXT, "dob" TEXT, "gender" TEXT, "aadhaar" TEXT, "blood" , "state" TEXT, "city" TEXT, "district" TEXT, "pin" TEXT, "addr1" TEXT, "addr2" TEXT, PRIMARY KEY("id") )''')
conn.execute('''CREATE TABLE IF NOT EXISTS HOSPITALS (NAME VARCHAR (100), MOB TEXT, "state" TEXT, "city" TEXT, "district" TEXT, "pin" TEXT, "addr1" TEXT, "addr2" TEXT) ''')
conn.execute('''CREATE TABLE IF NOT EXISTS "labs" ( id varchar (20) primary key not null, "licenseno" VARCHAR(15) NOT NULL, "pasw" VARCHAR NOT NULL, "labname" TEXT,ownername varchar(60), "tests_avlbl" TEXT, "email" TEXT, "mob" TEXT, "state" TEXT, "city" TEXT, "district" TEXT, "pin" TEXT, "addr1" TEXT, "addr2" TEXT )''')
conn.close()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = "secret key"
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'ndhp.gov@gmail.com'
    app.config['MAIL_PASSWORD'] = '12345Test@'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        db.create_all()

        #Registering blueprints on App
        import blueprint
        import login_blueprints
        import register_blueprints
        import indi_dashboard_blueprints
        app.register_blueprint(blueprint.main_bp)
        app.register_blueprint(login_blueprints.login_bp)
        app.register_blueprint(register_blueprints.register_bp)
        app.register_blueprint(indi_dashboard_blueprints.indi_dashboard_bp)
        return app
