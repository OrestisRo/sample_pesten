class Player:
	name =""
	hand = []

	def __init__(self, name):
		self.name = name

	def getHand(self):
		return self.hand

	def setHand(self, hand):
		self.hand = hand

	def drawCard(self, card):
		self.hand.append(card)
		print(self.name , "can't play and draws" , card)

	def playCard(self, index):
		card = self.hand.pop(index-1)
		print("%s plays %s (%s cards in hand remaining)" %(self.name, card, len(self.getHand())))
		return card

	def handToString(self):
		return (', '.join("%s%s" % (card.getValue(), card.getSuit()) for card in self.hand))

	def playOrDraw(self, topCard):
		print("%s's hand is: %s" %(self.name, self.handToString()))
		for card in self.hand:
			if (topCard.getValue() == card.getValue() or topCard.getSuit() == card.getSuit()):
				return self.hand.index(card)+1
		return 0

	def checkWin(self):
		if(len(self.hand) == 0):
			print(self.name + " wins!!!")
			return 1
		return 0

