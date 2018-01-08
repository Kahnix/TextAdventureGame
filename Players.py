class Player:
	def __init__(self,health,damage,hunger,thirst):
		self.health = health
		self.damage = damage
		self.hunger = hunger
		self.thirst = thirst

	def __str__(self):
		return \
		"""
		Name: {}\n
		Health:{}\n
		Damage:{}\n
		Hunger: {}\n
		Thirst:{}\n
		""".format(self.name, self.health, self.damage, self.hunger, self.thirst)

	def Eat(self, food):
		self.health += food.heal
		print("The " + food.name + " healed you for " + str(food.heal) + " hp, and your current hp is now " + str(self.health))