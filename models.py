from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy  import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()
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

	def get_name(self):
		name = self.fname + " " + self.lname
		return name


#_____________Added by eshan___________

class doctor(UserMixin, db.Model):
	uid = db.Column(db.String(10), primary_key = True, nullable = False)
	fname = db.Column(db.String(30), index = False, nullable= False)
	lname = db.Column(db.String(30), index = False, nullable= False)
	email = db.Column(db.String(30), index = False, nullable= False)
	mob = db.Column(db.String(30), index = False, nullable= False)
	dob = db.Column(db.String(30), index = False, nullable= False)
	gender = db.Column(db.String(30), index = False, nullable= False)
	regnum = db.Column(db.Integer(), index = False, nullable= False)
	Specialization = db.Column(db.Text(30), index = False, nullable= False)
	state = db.Column(db.String(15), index = False, nullable= False)
	city = db.Column(db.String(30), index = False, nullable= False)
	district = db.Column(db.String(30), index = False, nullable= True)
	pin = db.Column(db.Integer(), index = False, nullable= False)
	addr1 = db.Column(db.String(30), index = False, nullable= False)
	addr2 = db.Column(db.String(30), index = False, nullable= True)

	def get_doc(self):
		name = self.fname + " " + self.lname
		return name

#_____________.________________________

class labs(UserMixin, db.Model):
	id = db.Column(db.String(10), primary_key = True, nullable = False)
	licenseno = db.Column(db.String(10), index=False, nullable = False)
	pasw = db.Column(db.String(100), nullable = False)
	labname = db.Column(db.String(30), index = False, nullable= False)
	tests_avlbl = db.Column(db.String(30), index = False, nullable= False)
	email = db.Column(db.String(30), index = False, nullable= False)
	mob = db.Column(db.String(30), index = False, nullable= False)
	ownername = db.Column(db.String(30), index = False, nullable= False)
	state = db.Column(db.String(15), index = False, nullable= False)
	city = db.Column(db.String(15), index = False, nullable= False)
	district = db.Column(db.String(30), index = False, nullable= True)
	pin = db.Column(db.Integer(), index = False, nullable= False)
	addr1 = db.Column(db.String(30), index = False, nullable= False)
	addr2 = db.Column(db.String(30), index = False, nullable= True)

	def get_labname(self):
		name = self.labname
		return name
	def get_license(self):
		return self.licenseno
