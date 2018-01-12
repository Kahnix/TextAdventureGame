class Item:
  def __init__(self, name, description, weight, healthImpact, value):
    self.name = name
    self.description = description 
    self.weight = weight 
    self.healthImpact = healthImpact
    self.value = value
  
  def __str__(self):
    if self.healthImpact >= 0:
        return \
        "Name: {}\nDescription: {}\nCost: {}\nWeight: {}KG\nHeals: {}HP\n".format(self.name, self.description, self.weight, self.healthImpact)         
    else:
        return \
        "Name: {}\nDescription: {}\nCost: {}\nWeight: {}KG\nDamages: {}HP\n".format(self.name, self.description, self.weight, self.healthImpact)

class Inventory():
    def __init__(self):
        self.items={}

    def addItem(self, item):
        self.items[item.name] = item

    def __str__(self):
        out = '\t'.join(['Name','Description of Item\t','KG','healthImpact','value'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.description, item.weight, item.healthImpact, item.value]])
        return out