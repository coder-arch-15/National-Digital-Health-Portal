from flask import Blueprint, flash
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import new_user_credentials as nuc
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from models import individual
from flask_mail import Mail, Message
from PIL import Image, ImageDraw
import qrcode

########################################################################
#To add database code here
#ESHAN 321
#######################################################################
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

@main_bp.route('/forgot_password')
def forgot_pasw():
	message = "Hi "+fname+" " +lname+"\nYour login credentials for National Digital Health Portal are - \nUsername - " + h_id + "\nPassword - " + pasw
	msg = Message('NDHP Registration', sender = 'ndhp.gov@gmail.com', recipients = [email])
	msg.body = message
	mail.send(msg)
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

@main_bp.route('/login')
def login():
	return render_template('login.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():

	return render_template('dashboard.html', name = current_user.get_name())


@main_bp.route('/dashboard', methods = ['GET', 'POST'])
def login_submit():
	if request.method == 'POST':
		try:
			username = request.form['username']
			password = request.form['password']
			temp = individual.query.filter_by(id = username).first()
			if temp:
				if (check_password_hash(temp.pasw ,password)):
					login_user(temp)
					return redirect(url_for('main_bp.dashboard'))
				else:
					msg = "Incorrect"
					flash("Incorrect Password")
					return redirect(url_for('main_bp.login'))
			else:
				msg = "User not registered"
				flash("User not registered!")
				return redirect(url_for('main_bp.login'))

		except Exception as e:
			flash(e)
			return render_template('login.html')
			#msg = "Error in insert operation"



@main_bp.route('/logout')
@login_required
def logout():
	logout_user()
	msg = "You are logged out!"
	return redirect(url_for('main_bp.home'))


@main_bp.route('/individual_form_submit', methods = ['GET' , 'POST'])
def sub():
	if request.method == 'POST':
		try:
			fname = request.form['fname']
			lname = request.form['lname']
			email = request.form['email']
			mob = request.form['mob']
			dob = str(request.form['dob'])
			gender = request.form['gender']
			aadhaar = request.form['aadhaar']
			blood = request.form['blood']
			state = request.form['state']
			city = request.form['city']
			district = request.form['district']
			pin = request.form['pincode']
			addr1=request.form['add1']
			addr2=request.form['add2']

			nu = nuc.New_user(city, dob)
			h_id, pasw = nu.create_user()
			temp = individual(id=h_id, pasw=generate_password_hash(pasw) ,
				fname=fname, lname =lname, email=email, mob =mob, dob=dob,gender=gender,aadhaar=aadhaar, blood=blood,
				state=state, city=city, district=district, pin=pin, addr1=addr1, addr2=addr2 )
			db.session.add(temp)
			db.session.commit()

			thank_msg = "Record successfully added"
			message = "Hi "+fname+" " +lname+"\nThank You for registering with National Digital Health Portal.\nYour login credentials are - \nUsername - " + h_id + "\nPassword - " + pasw
			msg = Message('NDHP Registration', sender = 'ndhp.gov@gmail.com', recipients = [email])
			msg.body = message
			mail.send(msg)
			return render_template('thank.html',namee=thank_msg)

		except Exception as e:
			msg = e
			return render_template('thank.html',namee=msg)

#comment just to check if github is working or
#git hub working
