class Animal:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def speak(self):
		return "I am barking"


class Dog(Animal):
	def __init__(self, name, breed, color):
		super().__init__(name, breed)
		self.color = color


class Cat(Animal):
	pass


dog = Dog("Roxy", "Alsassian", "brown")
# cat = Cat()
# cat.speak()
# print(dog.speak())

print(dict(name=dog.name, breed=dog.breed, color=dog.color))
# print(cat.speak("I make meow"))
