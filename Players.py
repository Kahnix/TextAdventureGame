class Player:
	def __init__(self,health,damage,hunger,thirst):
		self.health = health
		self.damage = damage
		self.hunger = hunger
		self.thirst = thirst

	def __str__(self):
		return \
		"Health: {}\nDamage: {}\nHunger: {}\nThirst: {}\n".format(self.health, self.damage, self.hunger, self.thirst)

	def Eat(self, food):
		if food.healthImpact > 0:
			self.health += food.healthImpact
			print("The {} healed you for {}HP. Your  HP is now {}").format(food.name, str(food.healthImpact), str(self.health))
		else:
			self.health += food.healthImpact
			print("The {} was bad and damaged you for  {}HP. Your HP is now {}").format(food.name, str(food.healthImpact), str(self.health))

	def Attack(self,character):
		self.healthafter=character.health - self.damage

		if self.healthafter >0:
			print("You attacked {}. He loses {}HP").format(character.name, str(self.damage))
		else:
			print("You've killed {}").format(character.name)


class NonPlayer:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage

	def __str__(self):
		return \
		"Name: {} \nHealth: {} \nDamage {}\n".format(self.name,self.health,self.damage)
	
	def Attack(self, player):
		player.health -= self.damage
		print("{} attacked you for {}HP. You now have {}HP").format(self.name, str(self.damage), str(player.health))

