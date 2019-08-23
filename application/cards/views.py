from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.cards.models import Card, Attribute
from application.decks.models import Deck

from application.cards.forms import CardForm

from sqlalchemy.sql import text

@app.route("/cards/new")
@login_required
def cards_form():
  return render_template("/cards/new.html", form = CardForm())


@app.route("/cards/", methods=["POST"])
@login_required
def cards_create():
  form = CardForm(request.form)
  
  if not form.validate():
    return render_template("cards/new.html", form = form)
  
  card = Card(form.name.data, form.card_class.data, form.mana.data, form.rarity.data)
  card.favourite = form.favourite.data
  card.attack = form.attack.data
  card.defence = form.defence.data
  card.text = form.text.data
  card.tribe = form.tribe.data
  card.account_id = current_user.id

  if form.taunt.data:
    attribute = Attribute("taunt")
    card.attributes.append(attribute)

  if form.charge.data:
    attribute = Attribute("charge")
    card.attributes.append(attribute)

  if form.divine_shield.data:
    attribute = Attribute("divine_shield")
    card.attributes.append(attribute)
  
  if form.battlecry.data:
    attribute = Attribute("battlecry")
    card.attributes.append(attribute)

  if form.deathrattle.data:
    attribute = Attribute("deathrattle")
    card.attributes.append(attribute)
  
  db.session().add(card)
  db.session().commit()

  return redirect(url_for("cards_index"))

@app.route("/cards/<card_id>/", methods=["POST"])
@login_required
def cards_set_favourite(card_id):
  card = Card.query.get(card_id)
  card.favourite = False if card.favourite else True
  db.session.commit()

  return redirect(url_for("cards_index"))

@app.route("/cards/modify/<card_id>/", methods=["GET"])
@login_required
def cards_modify_form(card_id):
  card = Card.query.get(card_id)
  if card.account_id == current_user.id:
    return render_template("/cards/modify.html", form=CardForm(), card=card)
  return redirect(url_for("cards_index"))

@app.route("/cards/<card_id>/", methods=["GET"])
def cards_view(card_id):
  card = Card.query.get(card_id)  
  return render_template("/cards/view.html", card=card)

@app.route("/cards/modify/<card_id>/", methods=["POST"])
@login_required
def cards_modify(card_id):
  card = Card.query.get(card_id)
  form = CardForm(request.form)
  
  if not form.validate():
    return render_template("cards/modify.html", form = form)

  card.name = form.name.data
  card.card_class = form.card_class.data
  card.mana = form.mana.data
  card.rarity = form.rarity.data
  card.favourite = form.favourite.data
  card.attack = form.attack.data
  card.defence = form.defence.data
  card.text = form.text.data
  card.tribe = form.tribe.data

  db.session().commit()

  return redirect(url_for("cards_index"))

@app.route("/cards/delete/<card_id>", methods=["POST"])
@login_required
def cards_delete(card_id):

  card = Card.query.get(card_id)
  if card.account_id == current_user.id:
    db.session().delete(card)
    db.session().commit()

  return redirect(url_for("cards_index"))


@app.route("/cards/", methods=["GET"])
def cards_index():
  
  cards = Card.get_all()
  decks = Deck.query.all()

  cards_by_user = ""
  
  if current_user.is_authenticated:
    cards_by_user = Card.count_by_current_user()

  return render_template("cards/list.html", cards = cards, decks = decks, cards_by_user = cards_by_user)


@app.route("/cards/user/", methods=["GET"])
def cards_own():
  cards = Card.by_current_user()

  decks = Deck.query.all()
  cards_by_user = ""

  if current_user.is_authenticated:
    cards_by_user = Card.count_by_current_user()
  return render_template("cards/list.html", cards = cards, decks = decks, cards_by_user = cards_by_user)


@app.route("/cards/favourite/", methods=["GET"])
def cards_favourites():
  cards = Card.favourites()
  cards_by_user = ""

  if current_user.is_authenticated:
    cards_by_user = Card.count_by_current_user()
  decks = Deck.query.all()

  return render_template("cards/list.html", cards = cards, decks = decks, cards_by_user = cards_by_user)
