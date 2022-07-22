class Basket():

	def __init__(self, size: int) -> None:
		self._size = size - 1
		self._items = []

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, item_to_add):
		if len(self._items) <= self._size:
			self._items.append(item_to_add)
		elif len(self._items) > self._size:
			self._items.pop(0)
			self._items.append(item_to_add)


basket1 = Basket(4)
basket1.items = "Orange"
basket1.items = "Grape"
basket1.items = "Cashew"
basket1.items = "Cucumber"
basket1.items = "Berry"
basket1.items = "Cherry"


for item in basket1.items:
	print(item)

print(len(basket1.items))
print(basket1.items)
