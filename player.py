class Player:
	name =""
	hand = []

	def __init__(self, name):
		self.name = "Player "+ name

	def getHand(self):
		return self.hand

	def setHand(self, hand):
		self.hand = hand

	def addCard(self, card):
		self.hand.append(card)

	def playCard(self, index):
		self.hand.pop(index)