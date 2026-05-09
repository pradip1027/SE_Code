import unittest
def multiply(a, b):
    return a*b
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class MyTestClass(unittest.TestCase):
    def test_multiply_positive_numbers(self):
       result = multiply(3, 4)
       self.assertEqual(result, 12)

    def test_multiply_negative_numbers(self):
        result = multiply(-2, -5)
        self.assertEqual(result, 10)

    def test_multiply_zero(self):
        result = multiply(10, 0)
        self.assertEqual(result, 0)

    def test_multiply_with_one(self):
        result = multiply(7, 1)
        self.assertEqual(result, 7)

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -5), -7)

    def test_sub_positive_numbers(self):
        self.assertEqual(sub(10, 4), 6)

    def test_sub_negative_numbers(self):
        self.assertEqual(sub(-3, -5), 2)

    def test_divide(self):
        self.assertEqual(divide(4, 0), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()

