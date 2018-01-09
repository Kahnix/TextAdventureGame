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
		self.health += food.healthImpact
		print("The " + food.name + " healed you for " + str(food.healthImpact) + " hp, and your current hp is now " + str(self.health))

	def Attack(self,character):
		self.healthafter=character.health - self.damage

		if self.healthafter >0:
			print("You attacked "+character.name+" For " + str(self.damage) +", They now have " +str(character.health)+" health.")
		else:
			print("You attacked "+character.name+" For " + str(self.damage) +", They are now dead,")


class NonPlayable:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage

	def __str__(self):
		return \
		"Name: {} \nHealth: {} \nDamage {}\n".format(self.name,self.health,self.damage)

