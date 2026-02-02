"""
Card Game: 21 Boom 🃏
Objective
Build a simple two-player card game. The goal is to get as close as possible to 21 without going over

Card Rules
Number cards → value is the number
J / Q / K → value is 10
A (Ace) → value is 1
Use this code to generate random cards: click here
Game Setup
There are 2 players: Player 1 and Player 2
Each player starts with 2 random cards
Each player plays one at a time
Player Turn Rules
During a player turn:

Show the current cards and total value
Ask the player to choose:
0 = STOP
1 = CONTINUE
If the player chooses CONTINUE (1) → give one more card
If the player chooses STOP (0) → end the turn
If total equals 21 → instant win
If total is greater than 21 → player is disqualified
Game Flow
Player 1 plays first
Player 1 keeps choosing STOP or CONTINUE until:

they stop
reach 21
or are disqualified
Player 2 plays second
Player 2 plays only after Player 1 finishes
Same rules apply
Winner Decision
If one player is disqualified → the other player wins

If both players are valid:

the player closer to 21 wins
If both totals are equal → draw
"""


import random

# choose 10 random cards
for _ in range(10):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print("Your card is:", card, suit)