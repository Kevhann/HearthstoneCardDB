from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.decks.models import Deck
from application.cards.models import Card
from application.decks.forms import DeckForm

from sqlalchemy.sql import text

@app.route("/decks/new")
@login_required
def decks_form():
  return render_template("decks/new.html", form = DeckForm())

@app.route("/decks/", methods=["POST"])
@login_required
def decks_create():
  form = DeckForm(request.form)
  
  if not form.validate():
    return render_template("decks/new.html", form = form)
  
  deck = Deck(form.name.data, form.description.data, form.deck_class.data, current_user.id)
  deck.account_id = current_user.id
  deck.favourite = form.favourite.data 

  db.session().add(deck)
  db.session().commit()

  return redirect(url_for("decks_index"))

@app.route("/decks/favourite/<deck_id>/", methods=["POST"])
@login_required
def decks_set_favourite(deck_id):
  deck = Deck.query.get(deck_id)
  deck.favourite = False if deck.favourite else True
  db.session.commit()

  return redirect(url_for("decks_index"))

@app.route("/decks/<card_id>/", methods=["POST"])
def decks_add_card_to_deck(card_id):

  deck_id = request.form['deck_id']
  if deck_id != "Choose deck":
    card = Card.query.get(card_id)
    deck = Deck.query.get(deck_id)
    deck.cards.append(card)
    db.session.commit()

  return redirect(url_for("cards_index"))

@app.route("/decks/modify/<deck_id>/", methods=["GET"])
@login_required
def decks_modify_form(deck_id):
  deck = Deck.query.get(deck_id)  
  return render_template("/decks/modify.html", form=DeckForm(), deck=deck)

@app.route("/decks/<deck_id>/", methods=["GET"])
def decks_view(deck_id):
  deck = Deck.query.get(deck_id)  
  length = len(deck.cards)
  return render_template("/decks/view.html", deck=deck, length = length)

@app.route("/decks/modify/<deck_id>/", methods=["POST"])
@login_required
def decks_modify(deck_id):
  deck = Deck.query.get(deck_id)
  form = DeckForm(request.form)
  
  if not form.validate():
    return render_template("decks/modify.html", form = form)
  
  deck.name = form.name.data
  deck.deck_class = form.deck_class.data
  deck.favourite = form.favourite.data
  deck.description = form.description.data

  db.session().commit()

  return redirect(url_for("decks_index"))

@app.route("/decks/delete/<deck_id>", methods=["POST"])
@login_required
def decks_delete(deck_id):

  deck = Deck.query.get(deck_id)
  db.session().delete(deck)
  db.session().commit()

  return redirect(url_for("decks_index"))

@app.route("/decks/", methods=["GET"])
def decks_index():
  decks = Deck.get_all()
  decks_by_user = ""
  if current_user.is_authenticated:
    decks_by_user = Deck.count_by_current_user()
  return render_template("decks/list.html", decks = decks, decks_by_user = decks_by_user)

@app.route("/decks/user/", methods=["GET"])
def decks_own():
  decks = Deck.by_current_user()
  decks_by_user = ""
  if current_user.is_authenticated:
    decks_by_user = Deck.count_by_current_user()

  return render_template("decks/list.html", decks = decks, decks_by_user = decks_by_user)


@app.route("/decks/favourite/", methods=["GET"])
def decks_favourites():
  decks = Deck.favourites()
  decks_by_user = ""
  if current_user.is_authenticated:
    decks_by_user = Deck.count_by_current_user()

  return render_template("decks/list.html", decks = decks, decks_by_user = decks_by_user)
