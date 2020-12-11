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
	return render_template('doctor_register.html')

#@main_bp.route('/login')
#def login():
	#return render_template('login.html')

@main_bp.route('/dashboard') 		############Dashboard for individual
@login_required
def dashboard():
	return render_template('dashboard.html', name = current_user.get_name())

@main_bp.route('/dashboard3')		###########Dashboard for doctor
@login_required
def dr_dashboard():
	return render_template('doctor_dashboard.html', name = current_user.get_name())






@main_bp.route('/logout')
@login_required
def logout():
	logout_user()
	msg = "You are logged out!"
	return redirect(url_for('main_bp.home'))




@main_bp.route('/dashboard/settings')		###########Dashboard settings for individual
@login_required
def dashboard_settings():
	return render_template('settings.html', )


@main_bp.route('/dashboard/settings/update', methods = ['GET','POST'])		###########Dashboard settings update  button route for individual
@login_required
def dashboard_settings_update():
	if request.method == 'POST':
		try:
			current_user.fname = request.form['fname']
			current_user.lname = request.form['lname']
			current_user.mob = request.form['mob']
			current_user.dob = str(request.form['dob'])
			if(request.form.get('gender')):
				current_user.gender = request.form['gender']
			if(request.form.get('blood')):
				current_user.blood = request.form['blood']
			if(request.form.get('state')):
				current_user.state = request.form['state']
			if(request.form.get('city')):
				current_user.city = request.form['city']
			current_user.district = request.form['district']
			current_user.pin = request.form['pincode']
			current_user.addr1=request.form['add1']
			current_user.addr2=request.form['add2']
			if(request.form.get('upd_pasw')):
				current_user.pasw = generate_password_hash(request.form['upd_pasw'])

			message = "Hi "+current_user.fname+" " +current_user.lname+"\nYour account information has been updated on National Digital Health Portal."
			msg = Message('NDHP Registration', sender = 'ndhp.gov@gmail.com', recipients = [current_user.email])
			msg.body = message
			db.session.merge(current_user)
			db.session.commit()
			mail.send(msg)
			flash("Changes saved successfully!")
			return redirect(url_for('main_bp.dashboard_settings'))

		except Ecurrent_userception as e:
			flash(e)
			return redirect(url_for('main_bp.dashboard_settings'))


