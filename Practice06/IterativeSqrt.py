import unittest


def sqrt(x, accuracy):
    def sqrt_iter(guess):
        if good_enaugh(guess):
            guess = round(guess, 3)
            return guess
        else:
            return sqrt_iter(improve(guess))

    def improve(guess):
        return average(guess, x / guess)

    def average(x, y):
        return (x + y) / 2

    def good_enaugh(guess):
        if abs(guess ** 2 - x) < 10 ** (-accuracy):
            return 1
        else:
            return 0

    return sqrt_iter(1.0)


class TestSqrt(unittest.TestCase):
    def test_0(self):
        x = 2
        accuracy = 3
        result = 1.414
        self.assertEqual(sqrt(x, accuracy), result)

    def test_1(self):
        x = 4
        accuracy = 5
        result = 2
        self.assertEqual(sqrt(x, accuracy), result)

    def test_2(self):
        x = 6
        accuracy = 10
        result = 2.449
        self.assertEqual(sqrt(x, accuracy), result)

    def test_3(self):
        x = 225
        accuracy = 3
        result = 15
        self.assertEqual(sqrt(x, accuracy), result)

    def test_4(self):
        x = 625
        accuracy = 1
        result = 25.002
        self.assertEqual(sqrt(x, accuracy), result)

    def test_5(self):
        x = 100
        accuracy = 0
        result = 10.033
        self.assertEqual(sqrt(x, accuracy), result)


if __name__ == '__main__':
    unittest.main()
