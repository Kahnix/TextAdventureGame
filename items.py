class Items:
	def __init__(self, name, description, weight, heal, damage):
		self.name = name
		self.description = description 
		self.weight = weight 
		self.heal = heal
		self.damage = damage
	def __str__(self):
		return \
		"Item name: " + self.name + "\n" \
		+ "Item description: " + self.description + "\n" \
		+ "Item weight: " + self.weight + "\n" \
		+ "Item heal Ammount: " + self.heal + "\n" \
		+ "Item damage Ammount: " + self.damage