"""
Card Game: WAR
Objective
Build a simple card game between a player and the computer
The goal is to be the first to reach 10 points

Game Rules
The player gets one random card

The computer gets one random card

Card values:

A (Ace) → highest
K (King)
Q (Queen)
J (Jack)
10, 9, 8, .... 2
Use this code to generate random cards: click here

Scoring Rules
Player card > Computer card → Player gets +1 point
Computer card > Player card → Computer gets +1 point
Draw (same value) → 0 points to both
Game Flow
Start both scores at 0

Repeat rounds:

Deal one card to the player
Deal one card to the computer
Show both cards and their values
Update scores according to the rules
The game ends when:

Player score reaches 10 → Player wins
Computer score reaches 10 → Computer wins
"""



import random

# choose 10 random cards
for _ in range(10):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print("Your card is:", card, suit)