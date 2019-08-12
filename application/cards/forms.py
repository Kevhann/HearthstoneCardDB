from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField, validators

class CardForm(FlaskForm):
  name = StringField("Card name", [validators.Length(min=2)])
  text = TextAreaField("Card text")
  attack = IntegerField("Attack value")
  mana = IntegerField("Mana cost")
  defence = IntegerField("Defence value")
  rarity = SelectField(u"Rarity", choices=[("Free","Free"),("Common", "Common"),("Rare", "Rare"),("Epic", "Epic"),("Legendary", "Legenadry")])
  card_class = SelectField(u"Class", choices=[("Neutral","Neutral"),("Druid","Druid"),("Hunter","Hunter"),("Mage","Mage"),("Paladin","Paladin"),("Priest","Priest"),("Rogue","Rogue"),("Shaman","Shaman"),("Warrior","Warrior"),("Warlock","Warlock")])
  tribe = StringField("Card tribe")
  favourite = BooleanField("Favourite")
  class Meta:
    csrf = False



# kyseenalainen vulnerability jätetty päälle