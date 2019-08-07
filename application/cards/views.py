from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required
from application.cards.models import Card
from application.cards.forms import CardForm

@app.route("/cards/new")
@login_required
def cards_form():
  return render_template("cards/new.html", form = CardForm())

@app.route("/cards/", methods=["POST"])
@login_required
def cards_create():
  form = CardForm(request.form)
  
  if not form.validate():
    return render_template("cards/new.html", form = form)

  card = Card(form.name.data)
  card.favourite = form.favourite.data
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


@app.route("/cards/", methods=["GET"])
def cards_index():
  return render_template("cards/list.html", cards = Card.query.all())