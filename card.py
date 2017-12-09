# -*- coding: utf-8 -*-
import sys
from random import shuffle
from enum import Enum

class Suit(Enum):
	SPADES = u'♠'
	DIAMOND = u'♦'
	CLUBS = u"♣"
	HEARTS = u'♥'

class Card:
	value = ""
	suit = ""

	def __init__(self, value, suit):
		self.value = value
		self.suit = Suit(suit)

	def __str__(self):
		return str(self.value) + u"".join(self.suit.value)

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit.value

class Deck:
	top = 0
	cards = []
	pile = []

	def deckInit(self):
		suits = list(Suit)
		self.cards = [Card(value, suit) for value in range(1, 14) for suit in suits]

	def draw(self):
		card = self.cards[0]
		del self.cards[0]
		return card

	def dealHand(self):
		hand = self.cards[0:5]
		del self.cards[0:5]
		return hand

	def addToPile(self, card):
		self.pile.append(card)
		return self.getLastPlayedCard()

	def getLastPlayedCard(self):
		return self.pile[-1]

	def checkStatus(self):
		if (len(self.cards)<1):
			print("The game is over and ended with a tie...")
			return 1
		return 0
