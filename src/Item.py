class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return (f"\nName: {self.name}\nDescription: {self.description}\nWeight:{self.weight}")

    def __repr__(self):
        return str(self)

class Consumable(Item):
    def __init__(self, name, description, weight, healthImpact):
        super().__init__(name, description, weight)
        self.healthImpact = healthImpact

    def __str__(self):
        if self.healthImpact > 0:
            return (f"{super(Consumable, self).__str__()}\nHeals: {self.healthImpact}")
        else:
            return (f"{super(Consumable, self).__str__()}\nDamages: {self.healthImpact}")

    def consume(self, name, healthImpact):
        return


class Weapon(Item):
    def __init__(self, name, description, weight, damage, damage_type):
        super().__init__(name, description, weight)
        self.damage = damage
        self.damage_type = damage_type

    def __str__(self):
        return (f"{super(Weapon, self).__str__()}\nDamage: {self.damage}\nDamage Type: {self.damage_type}")


def main():

    class Sandwich(Consumable):
        def __init__(self):
            self.name = "Sandwich"
            self.description = "A lovely BLT sandwich"
            self.weight = 0.5
            self.healthImpact = 10

    sandwich1 = Sandwich()
    print(sandwich1)


if __name__ == '__main__':
    main()
