import unittest

class MyCalc():
    def __init__(self):
        self.ans = 0
    def addition(self, a, b):
        ans = a+b
        print("Addition of {0}, {1} = {2}".format(a,b,ans))
        self.ans = ans

    def subtraction(self, a, b):
        ans = a-b
        print("Subtraction of {0}, {1} = {2}".format(a,b,ans))
        self.ans = ans

    def multiplication(self, a, b):
        ans = a*b
        print("Multiplied {0} with {1} = {2}".format(a,b,ans))
        self.ans = ans

    def division(self, a, b):
        try:
            ans = a/b
            print("Division of {0}, {1} = {2}".format(a,b,ans))
            self.ans = ans
        except ZeroDivisionError:
            print("division by zero is not possiable")

    def run(self, a, math_operator, b):
        if a == 'ans':
            a = self.ans
        if math_operator == "+":
            self.addition(a,b)
        elif math_operator == "-":
            self.subtraction(a,b)
        elif math_operator == "*":
            self.multiplication(a,b)
        elif math_operator == "/":
            self.division(a,b)

class TestMyCalc(unittest.TestCase):
    def test(self):
        self.calc = MyCalc()
        self.number_add_number()
        self.ans_add_number()
        self.number_sub_number()
        self.ans_sub_number()
        self.number_mult_number()
        self.ans_mult_number()
        self.number_div_number()
        self.ans_div_number()

    def number_add_number(self):
        self.calc.run(2, "+", 2)
        self.assertEqual(self.calc.ans, 4)

    def ans_add_number(self):
        self.calc.run(self.calc.ans, "+", 5)
        self.assertEqual(self.calc.ans, 9)

    def number_sub_number(self):
        self.calc.run(10, "-", 4)
        self.assertEqual(self.calc.ans, 6)

    def ans_sub_number(self):
        self.calc.run(self.calc.ans, "-", 2)
        self.assertEqual(self.calc.ans, 4)

    def number_mult_number(self):
        self.calc.run(2, "*", 12)
        self.assertEqual(self.calc.ans, 24)

    def ans_mult_number(self):
        self.calc.run(self.calc.ans, "*", 2)
        self.assertEqual(self.calc.ans, 48)

    def number_div_number(self):
        self.calc.run(20, "/", 2)
        self.assertEqual(self.calc.ans, 10.0)

    def ans_div_number(self):
        self.calc.run(self.calc.ans, "/", 5)
        self.assertEqual(self.calc.ans, 2.0)

