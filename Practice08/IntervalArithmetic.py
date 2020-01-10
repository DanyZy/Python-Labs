import unittest


class Interval:
    """Инициальизация интервала"""
    def __init__(self):
        self.l = None
        self.u = None
        self.c = None
        self.r = None
        self.p = None

    """Задание интервала с процентом погрешности"""
    def buildIntervalWithPercentage(self, center, percent):
        self.c = center
        self.p = percent
        self.l = self.c - (self.c * self.p / 100)
        self.u = self.c + (self.c * self.p / 100)
        if self.l > self.u:
            temp = self.l
            self.l = self.u
            self.u = temp
        self.r = (self.u - self.l) / 2
        return self

    """Задание интервала по верхней и нижней точке"""
    def buildIntervalWithLowerUpper(self, lower, upper):
        if lower > upper:
            temp = lower
            lower = upper
            upper = temp
        self.l = lower
        self.u = upper
        self.c = (self.l + self.u) / 2
        self.r = (self.u - self.l) / 2
        try:
            self.p = self.r * 100 / self.c
        except ZeroDivisionError:
            self.p = 0
        return self

    """Задание интервала с радиусом погрешносит"""
    def buildIntervalWithRadius(self, center, radius):
        self.c = center
        self.r = radius
        self.l = self.c - self.r
        self.u = self.c + self.r
        if self.l > self.u:
            temp = self.l
            self.l = self.u
            self.u = temp
        try:
            self.p = self.r * 100 / self.c
        except ZeroDivisionError:
            self.p = 0
        return self

    """Сравнение интервалов"""
    def __eq__(self, other):
        if self.l == other.l and self.u == other.u:
            return True
        return False

    """Сложение интервалов"""
    def __add__(self, other):
        a = self.l + other.l
        b = self.u + other.u
        return Interval().buildIntervalWithLowerUpper(a, b)

    """Вычитание интервалов"""
    def __sub__(self, other):
        a = self.l - other.u
        b = self.u - other.l
        return Interval().buildIntervalWithLowerUpper(a, b)

    """Умножение интервалов"""
    def __mul__(self, other):
        a = min(self.l * other.l, self.l * other.u, self.u * other.l, self.u * other.u)
        b = max(self.l * other.l, self.l * other.u, self.u * other.l, self.u * other.u)
        return Interval().buildIntervalWithLowerUpper(a, b)

    """Деление интервалов"""
    def __truediv__(self, other):
        try:
            a = self.l / other.l
            c = self.u / other.l
            b = self.l / other.u
            d = self.u / other.u
        except ArithmeticError:
            a = 0
            c = 0
            b = 0
            d = 0
        x = min(a, b, c, d)
        y = max(a, b, c, d)
        return Interval().buildIntervalWithLowerUpper(x, y)

    """Вывод интервала"""
    def show(self):
        print([round(self.l, 2), round(self.u, 2)])

    """Вввод интервала с радиусом"""
    def show_radius(self):
        print([round(self.c, 2), round(self.r, 2)])

    """Вывод интервала с процентом прогрешности"""
    def show_percentage(self):
        if self.p is None:
            print("[" + str(round(self.c, 2)) + ", " + str(0) + "%" + "]")
        else:
            print("[" + str(round(self.c, 2)) + ", " + str(round(self.p, 2)) + "%" + "]")

    """Формальное представление интервала"""
    def __repr__(self):
        return str([round(self.l, 2), round(self.u, 2)])


zero = Interval().buildIntervalWithLowerUpper(0, 0)
pos1 = Interval().buildIntervalWithLowerUpper(1, 2)
pos2 = Interval().buildIntervalWithLowerUpper(5, 6)
dual1 = Interval().buildIntervalWithLowerUpper(-3, 5)
dual2 = Interval().buildIntervalWithLowerUpper(-2, 2)
neg1 = Interval().buildIntervalWithLowerUpper(-6, -4)
neg2 = Interval().buildIntervalWithLowerUpper(-7, -1)
rdual1 = Interval().buildIntervalWithLowerUpper(3, -8)
rdual2 = Interval().buildIntervalWithLowerUpper(12, -7)
rad = Interval().buildIntervalWithRadius(10, 4.25)
per = Interval().buildIntervalWithPercentage(6.8, 10)
pos1.show()
pos1.show_radius()
pos1.show_percentage()
print("_______________________________")
pos2.show()
pos2.show_radius()
pos2.show_percentage()
print("_______________________________")
rad.show()
rad.show_radius()
rad.show_percentage()
print("_______________________________")
per.show()
per.show_radius()
per.show_percentage()
print("_______________________________")


class TestOfInterval(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(zero+zero, Interval().buildIntervalWithLowerUpper(0, 0))
        self.assertEqual(zero-zero, Interval().buildIntervalWithLowerUpper(0, 0))
        self.assertEqual(zero*zero, Interval().buildIntervalWithLowerUpper(0, 0))
        self.assertEqual(zero/zero, Interval().buildIntervalWithLowerUpper(0, 0))

    def test_add(self):
        self.assertEqual(pos1 + pos2, Interval().buildIntervalWithLowerUpper(6, 8))

    def test_sub(self):
        self.assertEqual(pos2 - pos1, Interval().buildIntervalWithLowerUpper(3, 5))
        self.assertEqual(pos1 - pos2, Interval().buildIntervalWithLowerUpper(-5, -3))

    def test_mul(self):
        self.assertEqual(pos1 * pos2, Interval().buildIntervalWithLowerUpper(5, 12))
        self.assertEqual(pos1 * neg1, Interval().buildIntervalWithLowerUpper(-12, -4))
        self.assertEqual(pos1 * dual1, Interval().buildIntervalWithLowerUpper(-6, 10))
        self.assertEqual(pos1 * rdual1, Interval().buildIntervalWithLowerUpper(-16, 6))
        self.assertEqual(rdual1 * rdual2, Interval().buildIntervalWithLowerUpper(-96, 56))

    def test_div(self):
        self.assertEqual(pos1 / pos2, Interval().buildIntervalWithLowerUpper(1 / 6, 2 / 5))
        self.assertEqual(dual1 / dual2, Interval().buildIntervalWithLowerUpper(5 / (-2), 5 / 2))
        self.assertEqual(neg1 / neg2, Interval().buildIntervalWithLowerUpper((-4) / (-7), (-6) / (-1)))
        self.assertEqual(rdual1 / rdual2, Interval().buildIntervalWithLowerUpper((-8) / (-7), (-8) / 12))

    def test_eq(self):
        self.assertTrue(pos1 == Interval().buildIntervalWithLowerUpper(1, 2))


if __name__ == "__main__":
    unittest.main()
