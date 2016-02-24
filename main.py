from game import Game
from player import Player

def main():
	players = []
	players.append(Player("samu","0000"))
	players.append(Player("eikka","1111"))
	players.append(Player("aliisa","2222"))
	players.append(Player("heikki","3333"))
	play = int(input("To play type: 1, to end type: 0\n"))
	i = 0
	while (play == 1):
		game = Game(players)
		while (not(game.gameEnd())):
			game.playRound()
			game.printScores()
		print("Game ended!")
		for player in players:
			print("{0} ::Rating:: {1}".format(player.name, player.rating))
		#play = int(input("To play type: 1, to end type: 0\n"))
		if i == 1000:
			play = 0
		i += 1
	players[3].profile()
	

if __name__ == "__main__":
	main()
