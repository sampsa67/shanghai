class Player:
	def __init__(self, name, pwd):
		self.name = name
		self.pwd = pwd
		self.rating = 1000
		self.games = 0
		self.points = 0
		self.place = [0,0,0,0] #1,2,3,4

	def profile(self):
		print("Name: " + self.name)
		print("Rating: " + str(self.rating))
		print("Games played: " + str(self.games))
		print("Points average per game: " + str(int(self.points/self.games)))
		print("I : " + str(self.place[0]) + " II; " + str(self.place[1]) + " III: " + str(self.place[2]) + " JUMBO!: " + str(self.place[3]))
