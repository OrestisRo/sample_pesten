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

class Deck:
	top = 0
	deck = []

	def deckInit(self):
		suits = list(Suit)
		deck = []
		deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

		return deck

	def draw(self):
		return self.pop(0)

	def dealHand(self):
		return self


