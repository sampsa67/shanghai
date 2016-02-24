from player import Player
from rating import Rating
import random #TODO remove

class Game:
	def __init__(self, players):
		self.p = players
		self.scores = {self.p[0] : 0, self.p[1] : 0, self.p[2] : 0, self.p[3] : 0}
		self.rounds = []
		self.n = 0

	def playRound(self):
		r = []
		for i in range(4): #TODO remove
			r.append(random.randint(0,200))
		#r.append(int(input("Points for {0}: ".format(self.p[0].name))))
		#r.append(int(input("Points for {0}: ".format(self.p[1].name))))
		#r.append(int(input("Points for {0}: ".format(self.p[2].name))))
		#r.append(int(input("Points for {0}: ".format(self.p[3].name))))
		i = 0
		for score in r:
			self.scores[self.p[i]] += score
			i += 1
		self.n += 1
		self.rounds.append(r)

	def gameEnd(self):
		if (self.n == 8):
			self.ladder()
		return self.n == 8

	def printScores(self):
		print("{0}\t{1}\t{2}\t{3}".format(self.p[0].name, self.p[1].name, self.p[2].name, self.p[3].name))
		for y in self.rounds:
			i = 0
			for x in y:
				print(x, sep='', end='')
				if i == 3:
					print()
				else:
					print(end='\t')
				i += 1
		print("Totals are:")
		for i in range(4):
			print(self.scores[self.p[i]],end='')
			if i == 3:
				print()
			else:
				print(end='\t')
			i += 1

	def ladder(self):
		s = sorted(self.scores, key=self.scores.get)
		rat = Rating()
		newR = rat.rate(s)
		for i in range(4):
			s[i].rating = round(newR[i])
			s[i].games += 1
			s[i].points += self.scores[s[i]]
			s[i].place[i] += 1
