from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import new_user_credentials as nuc
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)
db.create_all()
SQLALCHEMY_TRACK_MODIFICATIONS = False

class individual(UserMixin, db.Model):   

	id = db.Column(db.String(10), primary_key = True, nullable = False)
	pasw = db.Column(db.String(100), nullable = False)
	fname = db.Column(db.String(30), index = False, nullable= False)
	lname = db.Column(db.String(30), index = False, nullable= False)
	email = db.Column(db.String(30), index = False, nullable= False)
	mob = db.Column(db.String(30), index = False, nullable= False)
	dob = db.Column(db.String(30), index = False, nullable= False)
	gender = db.Column(db.String(30), index = False, nullable= False)
	aadhaar = db.Column(db.Integer())
	blood = db.Column(db.Text(3), index = False, nullable= False)
	state = db.Column(db.String(15), index = False, nullable= False)
	city = db.Column(db.String(15), index = False, nullable= False)
	district = db.Column(db.String(30), index = False, nullable= True)
	pin = db.Column(db.Integer(), index = False, nullable= False)
	addr1 = db.Column(db.String(30), index = False, nullable= False)
	addr2 = db.Column(db.String(30), index = False, nullable= True)



@login_manager.user_loader
def load_user(user_id):
	return individual.query.get(user_id)


@app.route('/')
def home():
	return render_template('dummy home.html')


@app.route('/individual_register')
def individual_register():
	return render_template('individual_register.html')


@app.route('/labs_register')
def hello_worl():
	return render_template('labs_register.html')

@app.route('/doctor_register')
def hello_world():
	return render_template('doctor_register.html')

@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/dashboard', methods = ['GET', 'POST'])
def login_submit():
	if request.method == 'POST':
		try:
			username = request.form['username']
			password = request.form['password']
			temp = individual.query.filter_by(id = username).first()
			if temp:
				if (check_password_hash(temp.pasw ,password)):
					login_user(temp)
					msg = "Login successful"
				else:
					msg = "Incorrect Password"
			else:
				msg = "User not registered!"

		except Exception as e: 
			msg = e
			#msg = "Error in insert operation"
		finally:
			return render_template('dummy_dashboard.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	msg = "You are logged out!"
	return render_template('thank.html', namee=msg)


@app.route('/individual_form_submit', methods = ['GET' , 'POST'])
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
			
			msg = "Record successfully added"
		except Exception as e: 
			msg = e

			#msg = "Error in insert operation"
		finally:
			return render_template('thank.html', namee=msg)



if __name__ == '__main__':
	app.run(port = 8000, debug = True)