class Item:
    def __init__(self, name, description, weight, healthImpact, value):
        self.name = name
        self.description = description
        self.weight = weight
        self.healthImpact = healthImpact
        self.value = value

    def __str__(self):
        if self.healthImpact >= 0:
            print(f"Name: {self.name}\n\
                    Description: {self.description}\n\
                    Cost:\ {self.value}\n\
                    Weight: {self.weight}KG\n\
                    Heals: {self.healthImpact}HP\n")
        else:
            print(f"Name: {self.name}\n\
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
