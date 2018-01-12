import Players
import Items
#self,health,damage,hunger,thirst
# itemvalues={
# 'Sandwich':Items.Item("Sandwich", "A bacon lettuce and tomato sandwich",1,10,100),
# 'Gone Off Sandwich':Items.Item("Gone Off Sandwich", "A bacon lettuce and tomato sandwich that tastes like ass",1,-10,100)


# }
kacper = Players.Player(1000, 200, 10, 10)
#(self, name, health, damage):
goon = Players.NonPlayer("Goon1",1200,10)
goon2 = Players.NonPlayer("Goon2",100,10)
#kacper.Eat(sandwich)

# kacper.Attack(goon)
# kacper.Attack(goon2)

inventory = Items.Inventory()
inventory.addItem(Items.Item("Sandwich", "Tastes like Bacom",1,10,100))
inventory.addItem(Items.Item("Gone Off Sandwich", "Tastes Like Ass",1,-10,100))
print(inventory)