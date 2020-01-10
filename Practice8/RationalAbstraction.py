import unittest


class Fraction:
    """Инициализация дроби"""
    def __init__(self, n, d):
        self.n = n
        self.d = d
        n / d

    """Получение дроби в виде числа с плавающей точкой"""
    def __float__(self):
        return self.n / self.d

    """Действия с дробями (сложение и вычитание)"""
    def operation(self, other, sign):
        self.n = self.n * other.d + sign * other.n * self.d
        self.d = self.d * other.d
        return self

    """Сложение дробей"""
    def __add__(self, other):
        return self.operation(other, 1)

    """Вычитание дробей"""
    def __sub__(self, other):
        return self.operation(other, -1)

    """Умножение дробей"""
    def __mul__(self, other):
        self.n *= other.n
        self.d *= other.d
        return self

    """Деление дробей"""
    def __truediv__(self, other):
        self.n *= other.d
        self.d *= other.n
        return self

    """Сравнение дробей"""
    def comparison(self, other, condition):
        self.gcd(self.n, self.d)
        other.gcd(other.n, other.d)
        temp = self.d
        self.cd(other.d)
        other.cd(temp)
        if self.n + bool(condition) + other.n:
            return True
        return False

    """=="""
    def __eq__(self, other):
        return self.comparison(other, "==")

    """<"""
    def __lt__(self, other):
        return self.comparison(other, "<")

    """>"""
    def __gt__(self, other):
        return self.comparison(other, ">")

    """<="""
    def __le__(self, other):
        return self.comparison(other, "<=")

    """>="""
    def __ge__(self, other):
        return self.comparison(other, ">=")

    """Вычисление наибольшего общего делителя и упрощение дроби"""
    def gcd(self, n, d):
        if n < 0 and d < 0:
            n *= -1
            d *= -1
        while n != 0 and d != 0:
            if n == 1 or n == -1 or d == 1 or d == -1:
                n = 1
                d = 0
                break
            if n > d:
                n %= d
            else:
                d %= n
        self.n //= n + d
        self.d //= n + d
        return self

    """Приведение к общему знаменателю"""
    def cd(self, d):
        self.n *= d
        self.d *= d
        return self

    """Строчный вывод дроби"""
    def output(self):
        self.gcd(self.n, self.d)
        return str(self.n) + "/" + str(self.d)


class TestFraction(unittest.TestCase):

    def testEg(self):
        self.assertTrue(Fraction(1, 2) == Fraction(-3, -6))
        self.assertTrue(Fraction(9, 15) == Fraction(6, 10))
        self.assertTrue(Fraction(1, 3) == Fraction(1, 3))

    def testLt(self):
        self.assertTrue(Fraction(1, 2) < Fraction(2, 3))
        self.assertTrue(Fraction(-1, 2) < Fraction(1, 2))
        self.assertTrue(Fraction(0, 2) < Fraction(2, 3))

    def testGt(self):
        self.assertTrue(Fraction(2, 3) > Fraction(1, 3))

    def testGe(self):
        self.assertTrue(Fraction(2, 3) >= Fraction(1, 3))
        self.assertTrue(Fraction(2, 3) >= Fraction(4, 6))

    def testLe(self):
        self.assertTrue(Fraction(1, 2) <= Fraction(2, 3))
        self.assertTrue(Fraction(2, 3) <= Fraction(2, 3))

    def testFloat(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(-1, 5)), -0.2)
        self.assertEqual(float(Fraction(10, 2)), 5)
        self.assertEqual(float(Fraction(3, -8)), -0.375)

    def testADD(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 6), Fraction(2, 3))
        self.assertEqual(Fraction(1, 2) + Fraction(1, -3), Fraction(1, 6))

    def testSUB(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(1, 6) - Fraction(1, 2), Fraction(-1, 3))

    def testSUB2(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(1, 6) - Fraction(1, 2), Fraction(-1, 3))
        self.assertEqual(Fraction(1, 3) - Fraction(1, 3), Fraction(0, 3))

    def testMUL(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(1, 2) * Fraction(2, 1), Fraction(1, 1))
        self.assertEqual(Fraction(1, 2) * Fraction(-1, 2), Fraction(-1, 4))
        self.assertEqual(Fraction(-1, 2) * Fraction(1, -2), Fraction(1, 4))

    def testDIV(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))

    def testZero(self):
        try:
            Fraction(2, 0)
            self.assertTrue(False)
        except ArithmeticError:
            pass

    def testOutput(self):
        self.assertEqual(Fraction(4, 9).output(), "4/9")


if __name__ == '__main__':
    unittest.main()
