from modules.de import de

class Joueur:
	def __init__(self, nbr_pion, attaq):
		self.nbr_pion = nbr_pion
		self.attaq = attaq
		self.min = 1 if attaq == True else 0

	def getNbrLancer(self):
		if(self.attaq == True):
			return min(3, self.nbr_pion-1)
		else:
			return min(2, self.nbr_pion)
	
	@staticmethod
	def lancer(nbr):
		res = []
		for i in range(0, nbr):
			res.append(de(1, 6))
		res.sort(reverse=True)
		return res