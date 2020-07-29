from modules.joueur import Joueur

# Parametres
nbr = {
	'games': 2000, # Nombre de parties
	'pions': [50, 40] # Nombre de pions, [0] => attaquant, [1] => défenseur
}


class Game:
	def __init__(self, pions):
		self.j1 = Joueur(pions[0], True)
		self.j2 = Joueur(pions[1], False)
		while (self.j1.nbr_pion > self.j1.min and self.j2.nbr_pion > self.j2.min):
			self.fight()

		if(self.j1.nbr_pion <= self.j1.min):
			self.state = 1
		elif(self.j2.nbr_pion <= self.j2.min):
			self.state = 0
		else:
			print('Bug 1')

	def fight(self):
		r1 = self.j1.lancer(self.j1.getNbrLancer())
		r2 = self.j2.lancer(self.j2.getNbrLancer())
		losses = self.getWinner(r1, r2)

		self.j1.nbr_pion += losses[0]
		self.j2.nbr_pion += losses[1]

	@staticmethod
	def getWinner(r1, r2):
		iter = min(len(r1), len(r2))
		losses = [0, 0]
		for i in range(0, iter):
			if(r1[i] > r2[i]):
				losses[1] -= 1
			else:
				losses[0] -= 1
		return losses

results = [0,0]

for i in range(0, nbr['games']):
	game = Game(nbr['pions'])
	results[game.state] += 1

print(f"Attaq wins {(results[0]/nbr['games'])*100}% of the time")
print(f"Defense wins {(results[1]/nbr['games'])*100}% of the time")