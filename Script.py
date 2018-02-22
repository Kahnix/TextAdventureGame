from src import Player
from src import Item
#self,health,damage,hunger,thirst
# itemvalues={
sandwich=Item.Item("Sandwich", "A bacon lettuce and tomato sandwich",1,10)
# 'Gone Off Sandwich':Items.Item("Gone Off Sandwich", "A bacon lettuce and tomato sandwich that tastes like ass",1,-10,100)
goneOff=Item.Item("Nasty Sandwich", "A bacon lettuce and tomato sandwich",1,10)


# }
kacper = Player.Player(1000, 200, 10, 10,[])
#(self, name, health, damage):
goon = Player.NonPlayer("Goon1",1200,10)
goon2 = Player.NonPlayer("Goon2",100,10)
kacper.Eat(sandwich)

kacper.pickupItem(sandwich)
kacper.pickupItem(goneOff)
kacper.checkInventory()