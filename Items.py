class Item:
  def __init__(self, name, description, weight, healthImpact):
    self.name = name
    self.description = description 
    self.weight = weight 
    self.healthImpact = healthImpact
  
  def __str__(self):
    if self.healthImpact >= 0:
        return \
        "Name: {}\nDescription: {}\nWeight: {}KG\nHeals: {}HP\n".format(self.name, self.description, self.weight, self.healthImpact)         
    else:
        return \
        "Name: {}\nDescription: {}\nWeight: {}KG\nDamages: {}HP\n".format(self.name, self.description, self.weight, self.healthImpact)
