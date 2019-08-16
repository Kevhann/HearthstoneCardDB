from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.cards.models import Card
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
  return render_template("/cards/modify.html", form=CardForm(), card=card)

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
  db.session().delete(card)
  db.session().commit()

  return redirect(url_for("cards_index"))


@app.route("/cards/", methods=["GET"])
def cards_index():
  
  cards = Card.query.all()
  decks = Deck.query.all()

  cards_by_user = ""
  
  if current_user.is_authenticated:
    statement = text("Select Count(Account.id) AS count From Account JOIN Card "
                      "ON Card.account_id = Account.id WHERE Account.id = :account_id").params(account_id = current_user.id)
    result = db.engine.execute(statement).fetchone()
    cards_by_user = result['count']

  return render_template("cards/list.html", cards = cards, decks = decks, cards_by_user = cards_by_user)


@app.route("/cards/user/", methods=["GET"])
def cards_own():
  statement = text("SELECT * FROM Card "
                    "WHERE card.account_id = :account_id").params(account_id = current_user.id)
  cards = db.engine.execute(statement)
  decks = Deck.query.all()

  return render_template("cards/list.html", cards = cards, decks = decks)


@app.route("/cards/favourite/", methods=["GET"])
def cards_favourites():
  statement = text("SELECT * FROM Card "
                    "WHERE favourite = 1")
  cards = db.engine.execute(statement)
  decks = Deck.query.all()

  return render_template("cards/list.html", cards = cards, decks = decks)
