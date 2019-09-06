## user stories

- All users need to be able to see all cards and decks in a list.

```SELECT * FROM Card```
```SELECT * FROM Deck```

- Decks should show the cards in them

```SELECT * FROM Deck JOIN Card ON Deck.id = Card.id```

- Creators want to be able to see their own creations

```SELECT * FROM Card WHERE deck.account_id = :account_id```
```SELECT * FROM Deck WHERE deck.account_id = :account_id```

- Creators also want to know how many cards they have created

```SELECT COUNT(Account.id) AS count FROM Account JOIN Card ON Card.account_id = Account.id WHERE Account.id = :account_id```

