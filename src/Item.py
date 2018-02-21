class Item:
    def __init__(self, name, description, value, weight, healthImpact):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self.healthImpact = healthImpact

    def __str__(self):
        if self.healthImpact >= 0:
            return(f"\
Name: {self.name}\n\
Description: {self.description}\n\
Cost: {self.value}\n\
Weight: {self.weight}KG\n\
Heals: {self.healthImpact}HP\n")

        else:
            return(f"\
Name: {self.name}\n\
Description: {self.description}\n\
Cost: {self.value}\n\
Weight: {self.weight}KG\n\
Damages: {self.healthImpact}HP\n")


class Inventory():
    def __init__(self):
        self.items = {}

    def __str__(self):
        out = '\t'.join(['Name', 'Description of Item\t',
                         'KG', 'healthImpact', 'value'])

        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name,
                                                      item.description,
                                                      item.weight,
                                                      item.healthImpact,
                                                      item.value]])
        return out

    def addItem(self, item):
        self.items[item.name] = item


thing = Item("BAD Food", "NOT Tasty", 15, 25, -20)
print(thing)
