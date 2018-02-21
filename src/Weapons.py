class weapon:
	def __init__(self):
		self.name = name
		self.type = genre
		self.weight = weight
		self.damage = damage
		self.description = description
		self.quality = quality
		self.cost = cost
		self.damageType = damageType
		self.durability = durability

class bluntWeapons(weapon):
	def __init__(self):
		self.bluntDamage = bluntDamage

class sharpWeapons(weapon):
	def __init__(self):
		self.sharpdamage = sharpdamage
	

class gun(weapon):
	def __init__(self):
		self.penetrationDamage = penetrationDamage










class excalibur(sharpWeapons):
	def __init__(self):
		super(excalibur, self).__init__()
		self.name = "excalibur"
		self.weight = 1587 #grams
		self.damage = (9,14)


class rusty_broadsword(sword):
	def __init__(self):
		super(rusty broadsword, self).__init__()
		self.name = "rusty broadsword"
		self.weight = 1500 #grams
		self.damage = (3,6)






