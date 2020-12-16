from flask import Blueprint, flash
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import new_user_credentials as nuc
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from models import individual,labs
#from models import doctor
from flask_mail import Mail, Message

main_bp = Blueprint('main_bp', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)

db = SQLAlchemy(app)
db.create_all()
SQLALCHEMY_TRACK_MODIFICATIONS = False

@login_manager.user_loader
def load_user(user_id):
	return individual.query.get(user_id)


@main_bp.route('/')
def home():
	return render_template('home.html')


@main_bp.route('/login')
def login():
	return render_template('login.html')


@main_bp.route('/individual_register')
def individual_register():
	return render_template('individual_register.html')


@main_bp.route('/labs_register')
def hello_worl():
	return render_template('labs_register.html')

@main_bp.route('/doctor_register')
def hello_world():
	return render_template('doctor_indi_check.html')



@main_bp.route('/logout')
@login_required
def logout():
	logout_user()
	msg = "You are logged out!"
	return redirect(url_for('main_bp.home'))


@main_bp.route('/dashboard3')		###########Dashboard for doctor
@login_required
def dr_dashboard():
	return render_template('doctor_dashboard.html', name = current_user.get_name())
