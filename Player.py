import Items

class Player:
	def __init__(self,health,damage,hunger,thirst):
		self.health = health
		self.damage = damage
		self.hunger = hunger
		self.thirst = thirst

	def __str__(self):
		return \
		"Name: {} \nHealth: {} \nDamage: {}\n \nHealth: {}\nThirst:{}\n".format(self.name,self.health,self.damage,self.hunger,self.thirst)


print(Sandwhich)