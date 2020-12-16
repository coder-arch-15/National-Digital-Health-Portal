import random

class New_user:
	Codes= {'BHOPAL': 'BPL', 'JABALPUR': 'JBP', 'GWALIOR': 'GWL', 'UJJAIN': 'UJN', 'BHOPAL HABIBGANJ': 'HBJ', 'INDORE': 'INDB', 'ITARSI': 'ET',
 		'SATNA': 'STA', 'BINA': 'BINA', 'KHANDWA': 'KNW', 'KATNI': 'KTE', 'SAUGOR': 'SGO', 'MAIHAR': 'MYR', 'MORENA': 'MRA', 'REWA': 'REWA', 'NAGDA': 'NAD',
 		'PIPARIYA': 'PPI', 'VIDISHA': 'BHS', 'BETUL': 'BZU', 'NARSINGHPUR': 'NU', 'KANPUR': 'CNB', 'CHANDAULI': 'DDU', 'JHANSI': 'JHS', 'LUCKNOW': 'LC',
 		'PRAYAGRAJ': 'PCOI', 'MATHURA': 'MTJ', 'GHAZIABAD': 'GZB', 'VARANASI': 'BSB', 'AGRA': 'AGC', 'GORAKHPUR': 'GKP', 'MORADABAD': 'MB',
 		'BAREILLY': 'BE', 'GONDA': 'GD', 'SAHARANPUR': 'SRE', 'BASTI': 'BST', 'TUNDLA': 'TDL', 'SHAHJEHANPUR': 'SPN'}

	numCounter = 0
	aplh1="A"
	aplh2="A"
	aplh3="D"
	def __init__(self, city, dob):
		New_user.numCounter+=1
		if (New_user.numCounter==1000):
			New_user.numCounter=0
			New_user.aplh1 = chr(ord(New_user.aplh1) + 1)
			if(ord(New_user.aplh1)==123):
				New_user.aplh1 = "A"
				New_user.aplh2 = chr(ord(New_user.aplh2) + 1)
				if(ord(New_user.aplh2)==123):
					New_user.aplh2 = "A"
					New_user.aplh3 = chr(ord(New_user.aplh3) + 1)

		self.unique_id = "I"+New_user.Codes[city.upper()] + New_user.aplh3 + New_user.aplh2 + New_user.aplh1 + str(random.randint(1,99))
		y,m,d = dob.split("-")
		self.pasw = d+m+y

	def create_user(nu):
		return nu.unique_id, nu.pasw
