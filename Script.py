import Players
import Items

sandwich = Items.Item("Sandwich", "A bacon lettuce and tomato sandwich", 5, 5, 0)
kacper = Players.Player(1000, 200, 10, 10)
kacper.Eat(sandwich)