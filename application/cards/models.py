from application import db

class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	tribe = db.Column(db.String(144), nullable=True)
	card_class = db.Column(db.String(144), nullable=False)
	attack =  db.Column(db.Integer, nullable=True)
	defence =  db.Column(db.Integer, nullable=True)
	mana =  db.Column(db.Integer, nullable=False)
	rarity =  db.Column(db.String(144), nullable=False)
	favourite = db.Column(db.Boolean, nullable=False)
	text = db.Column(db.String(255), nullable=True)


	def __init__(self, name, card_class, mana, rarity):
		self.name = name
		self.favourite = False
		self.card_class = card_class
		self.mana = mana
		self.rarity = rarity
