from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField, validators

class DeckForm(FlaskForm):
  name = StringField("Deck name", [validators.Length(min=2)])
  description = TextAreaField("Deck description")
  deck_class = SelectField(u"Class", choices=[("Druid","Druid"),("Hunter","Hunter"),("Mage","Mage"),("Paladin","Paladin"),("Priest","Priest"),("Rogue","Rogue"),("Shaman","Shaman"),("Warrior","Warrior"),("Warlock","Warlock")])
  favourite = BooleanField("Favourite")
  class Meta:
    csrf = False
