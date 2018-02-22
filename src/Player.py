class Player:
    def __init__(self, health, damage, hunger, thirst, inventory):
        self.health = health
        self.damage = damage
        self.hunger = hunger
        self.thirst = thirst
        self.inventory = []

    def __str__(self):
        return
        f"Health: {self.health}\n \
        Damage: {self.damage}\n \
        Hunger: {self.hunger}\n \
        Thirst: {self.thirst} \n \
        Current Items: {self.inventory}"

    def __repr__(self):
        return str(self)

    def Eat(self, food):
        if food.healthImpact > 0:
            self.health += food.healthImpact
            print(f"The {food.name} healed you for {str(food.healthImpact)}HP.\
            Your HP is now {str(self.health)}")
        else:
            self.health += food.healthImpact
            print(f"The {food.name} was bad and damaged you for \
            {str(food.healthImpact)}HP. Your HP is now {str(self.health)}")

    def Attack(self, character):
        self.healthafter = character.health - self.damage

        if self.healthafter > 0:
            print(f"You attacked {characer.name}. \
            He loses {str(self.damage)}HP")
        else:
            print(f"You've killed {characer.name}")

    def pickupItem(self, item):
            self.inventory.append(item)

    def checkInventory(self):
            print(self.inventory)
    
    def Sleep(self):
        if self.health <= 90:
            self.health += 10
            print("You rested and healed 10HP")
        else:
            print("You can't sleep now.")


class NonPlayer:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return
        f"Name: {self.name} \n \
        Health: {self.health} \n \
        Damage {self.damage}\n"

    def Attack(self, player):
        player.health -= self.damage
        print(f"{self.name} attacked you for {str(self.damage)}HP.\
        You now have {str(player.health)}HP")
