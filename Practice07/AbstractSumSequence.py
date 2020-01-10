import unittest


def summa(f, start, stop, step):
    if start < stop:
        return f(start) + summa(f, step(start), stop, step)
    return 0


class TestSumma(unittest.TestCase):
    def test_1(self):
        self.assertEqual(summa(lambda x: x % 3, 1, 100, lambda x: x + 2), 49)

    def test_2(self):
        self.assertEqual(summa(lambda x: x**2, 1, 5, lambda x: x + 1), 30)

    def test_pi(self):
        result = 1 / (1 * 3) + 1 / (5 * 7) + 1 / (9 * 11)
        self.assertEqual(summa(lambda x: 1 / (x * (x + 2)), 1, 10, lambda x: x + 4), result)


if __name__ == '__main__':
    unittest.main()
