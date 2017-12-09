from player import Player
from card import *

class Game:
	CONST_PLAYERNAMES = ['Alice', 'Bob', 'Carol', 'Eve']
	deck = Deck()
	players = []
	
	def __init__(self):
		print("---Starting new game.---")
		self.deck.deckInit()
		print("---A deck of 52 cards has been created.---")
		self.players = [Player(name) for name in self.CONST_PLAYERNAMES]
		print("---4 predefined players have been created.---")

def main():
	game = Game()
	shuffle(game.deck.cards)
	print("---The deck has been shuffled---")
	print("---The players are being dealt hands---")
	for player in game.players:
		player.setHand(game.deck.dealHand())
		player.handToString()


	print("Deck opens a top card to the pile.")
	firstCard = game.deck.draw()
	game.deck.addToPile(firstCard)
	print("The top card is: ", firstCard)

	while(1):
		for player in game.players:
			print("The card on top is: ", game.deck.getLastPlayedCard())
			canPlay = player.playOrDraw(game.deck.getLastPlayedCard())
			if (canPlay):
				game.deck.addToPile(player.playCard(canPlay))
			else:
				player.drawCard(game.deck.draw())
			if (player.checkWin() or game.deck.checkStatus()):
				sys.exit(0)
			print()










if __name__ == "__main__":
	main()