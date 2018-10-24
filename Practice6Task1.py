import unittest


def fib(n):
    a = 0
    b = 1
    return iteration(a, b, n)


def iteration(a, b, count):
    if count == 0:
        return a
    return iteration(b, a + b, count - 1)


class TestFibonacchi(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fib(0), 0)

    def test_2(self):
        self.assertEqual(fib(1), 1)

    def test_3(self):
        self.assertEqual(fib(7), 13)


if __name__ == '__main__':
    unittest.main()
