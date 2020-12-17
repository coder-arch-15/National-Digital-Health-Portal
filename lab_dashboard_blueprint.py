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

indi_dashboard_bp = Blueprint('lab_dashboard_bp', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)

db = SQLAlchemy(app)
db.create_all()
SQLALCHEMY_TRACK_MODIFICATIONS = False

@login_manager.user_loader
def load_user(user_id):
	return individual.query.get(user_id)



@lab_dashboard_bp.route('/lab/dashboard') 		############Dashboard for lab
@login_required
def lab_dashboard():
	return render_template('lab_dashboard.html', cu = current_user)


@lab_dashboard_bp.route('/lab/dashboard/settings')		###########Dashboard settings for lab
@login_required
def dashboard_settings():
	return render_template('lab_settings.html', )


@lab_dashboard_bp.route('/dashboard/settings/update', methods = ['GET','POST'])		###########Dashboard settings update  button route for individual
@login_required
def dashboard_settings_update():
	if request.method == 'POST':
		try:
			current_user.lab_name = request.form['lab_name']
			current_user.tests_avlbl = request.form['tests_avlbl']
			current_user.mob = request.form['mob']
			current_user.email = request.form['email']
			current_user.owner_name = request.form['owner_name']
			current_user.licenseno = request.form['licenseno']
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

			message = "Hi "+current_user.lab_name+"\nYour account information has been updated on National Digital Health Portal."
			msg = Message('NDHP Registration', sender = 'ndhp.gov@gmail.com', recipients = [current_user.email])
			msg.body = message
			db.session.merge(current_user)
			db.session.commit()
			mail.send(msg)
			flash("Changes saved successfully!")
			return redirect(url_for('lab_dashboard_bp.dashboard_settings'))

		except Ecurrent_userception as e:
			flash(e)
			return redirect(url_for('lab_dashboard_bp.dashboard_settings'))


@lab_dashboard_bp.route('/lab/dashboard/search_dr')		###########Dashboard settings for doctor searcch
@login_required
def dashboard_search_dr():
	return render_template('indi_search_dr.html')

@indi_dashboard_bp.route('/indi/dashboard/search_lab')		###########Dashboard settings for doctor searcch
@login_required
def dashboard_search_lab():
	return render_template('indi_search_labs.html')