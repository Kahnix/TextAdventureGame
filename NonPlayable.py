class NonPlayable:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage

	def __str__(self):
		return \
		"Name: {} \nHealth: {} \nDamage {}\n".format(self.name,self.health,self.damage)


Miguel = NonPlayable("Miguel", 100, 10)
Kacper = NonPlayable("Kacper", 100, 10)

