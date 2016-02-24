from player import Player

class Rating:
	##
	#\brief A constructor
	#
	#Construct a new rating system (K value).
	#\return Nothing.
	def __init__(self):
		self.K = 32.
		self.N = 4.

	##
	#\brief Score in pairwise comparison
	#
	#Calculates the score expected if the match would be 1vs1
	#\param p Players rating
	#\param o Opponets rating
	#\return Expected result in 1vs1
	def pairComp(self, p, o):
		return 1./(1. + 10.**((o-p)/400.))
	##
	#\brief Rating calculator
	#
	#Method used to calculate new rating after the match.
	#\param p Players rating before the match.
	#\param o Ratings of all of the opponents before the match.
	#\param r Result aka place (1,2,...,N)
	#\return Players new rating
	def calRating(self, p, o, r):
		e = 0
		for opp in o:
			e += self.pairComp(p, opp)
		if r == 1:
			return p + self.K * (self.N -r - e)
		else:
			return p + self.K * (1-e)

	##
	#\brief New ratings
	#
	#Calculates new ratings for all the players
	#\param l Sorted list of players
	#\return List of new ratings
	def rate(self, l):
		s = []
		for i in range(4):
			r = i+1
			temp = []
			#if i == 0:
			#	r = 1
			for j in range(4):
				if (i != j):
					temp.append(l[j].rating)
			s.append(self.calRating(l[i].rating,temp,r))
		return s
