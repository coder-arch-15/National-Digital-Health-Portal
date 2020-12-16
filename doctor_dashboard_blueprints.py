from flask import Blueprint, flash
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import new_user_credentials as nuc
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from models import individual,labs,doctor
#from models import doctor
from flask_mail import Mail, Message

doctor_dashboard_bp = Blueprint('doctor_dashboard_bp', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)

db = SQLAlchemy(app)
db.create_all()
SQLALCHEMY_TRACK_MODIFICATIONS = False

@login_manager.user_loader
def load_user(user_id):
	return doctor.query.get(user_id)


@doctor_dashboard_bp.route('/doctor/dashboard') 		############Dashboard for doctor
@login_required
def doctor_dashboard():
	return render_template('doctor_dashboard.html')
