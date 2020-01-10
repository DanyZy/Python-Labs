import unittest


def fast_pow_rec(n, p):
    if p == 0:
        return 1
    elif p % 2 == 0:
        return fast_pow_rec(n * n, p / 2)
    else:
        return n * fast_pow_rec(n, p - 1)


def fast_pow_iter(n, p):
    return fast_pow_iter_main(n, p)


def fast_pow_iter_main(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    elif p % 2 == 0:
        return fast_pow_iter_main(n * n, p / 2)
    else:
        return n * fast_pow_iter_main(n, p - 1)


class TestFastPower(unittest.TestCase):
    def test_1(self):
        n = 10
        power = 0
        result = 1
        self.assertEqual(fast_pow_rec(n, power), result)
        self.assertEqual(fast_pow_iter(n, power), result)

    def test_2(self):
        n = 2
        power = 5
        result = 32
        self.assertEqual(fast_pow_rec(n, power), result)
        self.assertEqual(fast_pow_iter(n, power), result)

    def test_3(self):
        n = 3
        power = 3
        result = 27
        self.assertEqual(fast_pow_rec(n, power), result)
        self.assertEqual(fast_pow_iter(n, power), result)

    def test_4(self):
        n = 3
        power = 6
        result = 729
        self.assertEqual(fast_pow_rec(n, power), result)
        self.assertEqual(fast_pow_iter(n, power), result)

    def test_5(self):
        n = 0
        power = 10
        result = 0
        self.assertEqual(fast_pow_rec(n, power), result)
        self.assertEqual(fast_pow_iter(n, power), result)


if __name__ == '__main__':
    unittest.main()
