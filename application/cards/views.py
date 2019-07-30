from application import app, db
from flask import render_template, request, url_for, redirect
from application.cards.models import Card

@app.route("/cards/new")
def cards_form():
  return render_template("cards/new.html")

@app.route("/cards/", methods=["POST"])
def cards_create():
  card = Card(request.form.get("name"))
  db.session().add(card)
  db.session().commit()

  return redirect(url_for("cards_index"))

@app.route("/cards/<card_id>/", methods=["POST"])
def cards_set_favourite(card_id):
  card = Card.query.get(card_id)
  card.favourite = False if card.favourite else True
  db.session.commit()

  return redirect(url_for("cards_index"))


@app.route("/cards/", methods=["GET"])
def cards_index():
  return render_template("cards/list.html", cards = Card.query.all())