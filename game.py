from player import Player
from card import *

class Game:
	CONST_PLAYERNAMES = ['Alice', 'Bob', 'Carol', 'Eve']
	deck = []
	players = []
	
	def __init__(self):
		print("---Starting new game.---")
		self.deck = Deck().deckInit()
		print("---A deck of 52 cards has been created.---")
		self.players = [Player(name) for name in self.CONST_PLAYERNAMES]
		print("---4 predefined players have been created.---")

def main():
	game = Game()
	shuffle(game.deck)
	print("---The deck has been shuffled---")
	for player in game.players:
		player.setHand(game.deck.deal())



if __name__ == "__main__":
	main()