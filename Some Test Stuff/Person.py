class Person:
	def __init__(self, name, age, favorite_foods):
		self.name = name
		self.age = age
		self.favorite_foods = favorite_foods

	def __str__(self):
		return \
		"Name: " + self.name +"\n" \
		+ "Age: " + str(self.age) + "\n" \
		+ "Favourite food: " + str(self.favorite_foods[0])

	def birth_year(self):
		return 2018 - self.age

people = [
		Person("Kacper", 18, ["Maxx Crisps", "Redbull"]),
		Person("Miguel", 18, ["Ice cream", "Hot-dog"]),
		Person("Gutek", 15, ["Mid", "Pasta"])]

sum = 0
age_sum = 0
year_sum = 0
  
for person in people:
	age_sum = age_sum + person.age
	year_sum = year_sum + person.birth_year()
	
print("The average age is: " + str(age_sum / len(people)))
print("The average birth year is: " + str(int(year_sum / len(people))))
print(person)