## user stories

- As a casual browser, I want to be able to see all cards and decks in a list.
SQL statements:
```SELECT * FROM Card```
```SELECT * FROM Deck```
- As a Hearthstone player, I want to be able to browse all my cards and decks.
```SELECT * FROM Card```
```SELECT * FROM Deck```
- As a heavy user, i want to know how many cards I have created.
SQL statement:
```SELECT COUNT(Account.id) AS count FROM Account JOIN Card ON Card.account_id = Account.id WHERE Account.id = :account_id```
- As a strategic enthusiast, I want to sort and filter my cards by different metrics, including hp, mana cost and keywords.
Not supported
