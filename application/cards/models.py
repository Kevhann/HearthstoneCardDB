from application import db
from flask_login import current_user
from sqlalchemy.sql import text

attributes = db.Table('attributes',
    db.Column('attribute_id', db.Integer, db.ForeignKey('attribute.id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True)
)

class Attribute(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(144), nullable= False)

  def __init__(self, name):
    self.name = name


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
  attributes = db.relationship('Attribute', secondary=attributes, lazy='subquery', backref=db.backref('cards', lazy=True))

  account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)


  def __init__(self, name, card_class, mana, rarity):
    self.name = name
    self.favourite = False
    self.card_class = card_class
    self.mana = mana
    self.rarity = rarity
  
  def count_by_current_user():
    statement = text("Select Count(Account.id) AS count From Account JOIN Card "
                      "ON Card.account_id = Account.id WHERE Account.id = :account_id").params(account_id = current_user.id)
    result = db.engine.execute(statement).fetchone()
    return result['count']

  def get_all():
    statement = text("Select * From Card")
    result = db.engine.execute(statement).fetchall()
    return result

  def favourites():
    statement = text("SELECT * FROM Card "
                    "WHERE favourite = 1")
    cards = db.engine.execute(statement)
    return cards
    
  def by_current_user():
    statement = text("SELECT * FROM Card "
                    "WHERE card.account_id = :account_id").params(account_id = current_user.id)
    cards = db.engine.execute(statement)
    return cards
  