from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class CardForm(FlaskForm):
  name = StringField("Card name", [validators.Length(min=2)])
  favourite = BooleanField("Favourite")
  class Meta:
    csrf = False
# kyseenalainen vulnerability jätetty päälle