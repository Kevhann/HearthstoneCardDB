from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class CardForm(FlaskForm):
  name = StringField("Card name")
  favourite = BooleanField("Favourite")
  class Meta:
    csrf = False
# kyseenalainen vulnerability jätetty päälle