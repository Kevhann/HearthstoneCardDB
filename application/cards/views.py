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
  
  card = Card(form.name.data, form.card_class.data, form.mana.data, form.rarity.data)
  card.favourite = form.favourite.data
  card.attack = form.attack.data
  card.defence = form.defence.data
  card.text = form.text.data
  card.tribe = form.tribe.data
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

@app.route("/cards/modify/<card_id>/")
@login_required
def cards_modify_form(card_id):
  card = Card.query.get(card_id)  
  return render_template("/cards/modify.html", form=CardForm(), card=card)


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
  print("AFBEBOTJAOFJOQNVOASNBOASFNBO")
  print("AFBEBOTJAOFJOQNVOASNBOASFNBO")
  print("AFBEBOTJAOFJOQNVOASNBOASFNBO")
  print("AFBEBOTJAOFJOQNVOASNBOASFNBO")
  print("AFBEBOTJAOFJOQNVOASNBOASFNBO")

  card = Card.query.get(card_id)
  db.session().delete(card)
  db.session().commit()

  return redirect(url_for("cards_index"))


@app.route("/cards/", methods=["GET"])
def cards_index():
  return render_template("cards/list.html", cards = Card.query.all())
