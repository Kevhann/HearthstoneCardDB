from application import db
from flask_login import current_user
from sqlalchemy.sql import text

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

  def count_by_current_user():
    statement = text("Select Count(Account.id) AS count From Account JOIN Deck "
                      "ON Deck.account_id = Account.id WHERE Account.id = :account_id").params(account_id = current_user.id)
    result = db.engine.execute(statement).fetchone()
    return result['count']

  def get_all():
    statement = text("Select * From Deck")
    result = db.engine.execute(statement).fetchall()
    return result

  def favourites():
    statement = text("SELECT * FROM Deck "
                    "WHERE favourite = 1")
    decks = db.engine.execute(statement)
    return decks
    
  def by_current_user():
    statement = text("SELECT * FROM Deck "
                    "WHERE deck.account_id = :account_id").params(account_id = current_user.id)
    decks = db.engine.execute(statement)
    return decks