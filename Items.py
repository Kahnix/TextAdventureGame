class Items:
  def __init__(self, name, description, weight, healthImpact):
    self.name = name
    self.description = description 
    self.weight = weight 
    self.healthImpact = healthImpact
  
  def __str__(self):
    if self.healthImpact >= 0:
        return \
        "Item name: " + self.name + "\n" \
        + "Item description: " + self.description + "\n" \
        + "Weight: " + str(self.weight) + "G\n" \
        + "Heals: " + str(self.healthImpact) + " HP\n"
    else:
        return \
        "Item name: " + self.name + "\n" \
        + "Item description: " + self.description + "\n" \
        + "Weight: " + str(self.weight) + "G\n" \
        + "Damages: " + str(self.healthImpact) + " HP\n"
