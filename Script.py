import Players
import Items
#self,health,damage,hunger,thirst
sandwich = Items.Item("Sandwich", "A bacon lettuce and tomato sandwich",1,10)
kacper = Players.Player(1000, 200, 10, 10)
#(self, name, health, damage):
goon = Players.NonPlayable("Goon1",1200,10)
goon2 = Players.NonPlayable("Goon2",100,10)
#kacper.Eat(sandwich)

kacper.Attack(goon)
kacper.Attack(goon2)