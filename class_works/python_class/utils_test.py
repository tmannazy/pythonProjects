import unittest
from utils import *


class MyTestCase(unittest.TestCase):
	def setUp(self) -> None:
		print("I run before every test case")

	@classmethod
	def setUpClass(cls) -> None:
		print("I run once before all since it's a class")

	@classmethod
	def tearDownClass(cls) -> None:
		print("I run after all first")

	def tearDown(self) -> None:
		print("I run after every test case")

	def test_something(self):
		self.assertEqual(True, True)  # add assertion here

	def test_add_test(self):
		"""
		Given:

		When:

		Then:

		"""
		self.assertAlmostEqual(5, add(2, 3))

	def test_list(self):
		self.assertEqual([1, 4, 9], square_list([1, 2, 3]))

	def test_for_error(self):
		with self.assertRaisesRegex(TypeError, "function return") as f:
			add(3, "6")

		self.assertRaisesRegex(TypeError, "function return", add, [4], 2)

	def test_for_type_error(self):
		with self.assertRaises(TypeError) as d:
			add(3, [5])


if __name__ == '__main__':
	unittest.main()
