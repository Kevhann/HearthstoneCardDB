from application import db

class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	favourite = db.Column(db.Boolean, nullable=False)

	def __init__(self, name):
		self.name = name
		self.favourite = False
