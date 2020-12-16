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

login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)
db = SQLAlchemy(app)
db.create_all()
SQLALCHEMY_TRACK_MODIFICATIONS = False


login_bp = Blueprint('login_bp', __name__)

@login_manager.user_loader
def load_user(user_id):
	return individual.query.get(user_id)



@login_bp.route('/login_submit', methods = ['GET', 'POST'])
def login_submit():
	if request.method == 'POST':
		try:
			username = request.form['username']
			password = request.form['password']
			if(username[0]=="I"):
				temp = individual.query.filter_by(id = username).first()
				if temp:
					if (check_password_hash(temp.pasw ,password)):
						login_user(temp)
						return redirect(url_for('indi_dashboard_bp.indi_dashboard'))
					else:
						msg = "Incorrect"
						flash("Incorrect Password")
						return redirect(url_for('main_bp.login'))
			elif(username[0]=="D"):
				temp = doctor.query.filter_by(id = username).first()		####replace individual with doctor
				if temp:
					if (check_password_hash(temp.pasw ,password)):
						login_user(temp)
						return redirect(url_for('doctor_dashboard_bp.doctor_dashboard'))  ### see here
					else:
						msg = "Incorrect"
						flash("Incorrect Password")
						return redirect(url_for('main_bp.login'))

			elif(username[0]=="L"):
				temp = individual.query.filter_by(id = username).first()		####replace individual with labs
				if temp:
					if (check_password_hash(temp.pasw ,password)):
						login_user(temp)
						return redirect(url_for('indi_dashboard_bp.indi_dashboard'))
					else:
						msg = "Incorrect"
						flash("Incorrect Password")
						return redirect(url_for('main_bp.login'))
			else:
				msg = "Invalid User ID!"
				flash("Invalid User ID!")
				return redirect(url_for('main_bp.login'))

			msg = "User not registered"
			flash("User not registered!")
			return redirect(url_for('main_bp.login'))

		except Exception as e:
			flash(e)
			return render_template('login.html')
			#msg = "Error in insert operation"


@login_bp.route('/forgot_password')
def forgot_pasw():
	message = "Hi "+fname+" " +lname+"\nYour login credentials for National Digital Health Portal are - \nUsername - " + h_id + "\nPassword - " + pasw
	msg = Message('NDHP Registration', sender = 'ndhp.gov@gmail.com', recipients = [email])
	msg.body = message
	mail.send(msg)
	return render_template('login.html')
