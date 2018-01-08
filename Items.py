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
    + "Weight: " + str(self.weight) + "G\n" \
    + "Heals: " + str(self.heal) + " HP\n" \
    + "Damages: " + str(self.damage) + " HP"
