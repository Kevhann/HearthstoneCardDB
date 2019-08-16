from application import db

cards = db.Table('cards',
    db.Column('deck_id', db.Integer, db.ForeignKey('deck.id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True)
)



class Deck(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	full = db.Column(db.Boolean, nullable=False)
	favourite = db.Column(db.Boolean, nullable=False)

	description = db.Column(db.String(1024), nullable=False)
	deck_class = db.Column(db.String(144), nullable=False)
	account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

	cards = db.relationship('Card', secondary=cards, lazy='subquery', backref=db.backref('decks', lazy=True))

	def __init__(self, name, description, deck_class, account_id):
		self.name = name
		self.full = False
		self.description = description
		self.deck_class = deck_class
		self.account_id = account_id
