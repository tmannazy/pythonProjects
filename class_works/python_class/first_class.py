# class MyClass:
# var = 'From the class'


# class AnotherClass:
# 	pass

#
# first = MyClass()
# second = MyClass()
# print(first)
# first.var = 'A variable'
#
# print(first.var)
# print(second.var)

# from typing import NewType


# class MyClass:
# 	def a_method(self):  # instance method
# 		pass
#
#
# my_class = MyClass()
#
# my_class.a_method()


class Person:
	number_of_persons = 0

	def __init__(self, name: str, age=17) -> None:
		# self.__name = name
		self._name = name  # with line 42
		self.__age = 17  # with line 60
		self._age = age

	@classmethod
	def get_number_of_persons(cls):
		return cls.number_of_persons

	@staticmethod
	def determine_class(age: int) -> str:
		if age >= 18:
			return 'Major'
		return "Minor"


	@property
	def name(self):
		print("You're calling me")
		# return self.__name
		return self._name

	# return self._name  # with line 36

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, new_age):
		if new_age < 0:
			raise ValueError("Age cannot be negative")
		self._age = new_age

	@name.setter  # decorator
	def name(self, name):
		print("Setter done")
		if 'f' in name:
			print("Fuck off")
			self._name = name

	@name.deleter  # decorator
	def name(self):
		print("Name will be deleted")
		del self._name


person1 = Person("Abigail")
person1.name = "Omotee"
print(person1.name)

# del person1.name
# person1.age = 55
# print(person1.name)
# print(person1.age)

print(Person.number_of_persons)
print(person1.number_of_persons)
person1.number_of_persons = 8
print(person1.number_of_persons)

# print(dir(person1))  # with lines 36 & 42
# print(person1._Person__name)  # with line 42
# print(person1._Person__age)  # with line 37


# @print
# @str.upper
# def print_str(string):
# 	return string
