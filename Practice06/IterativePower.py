import unittest


def pow_rec(n, p):
    if p == 0:
        return 1
    return n * pow_rec(n, p - 1)


def pow_iter(n, p):
    return pow_iter_main(n, p)


def pow_iter_main(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    return n * pow_iter_main(n, p - 1)


class TestPower (unittest.TestCase):
    def test_rec(self):
        self.assertEqual(pow_rec(25, 2), 625)

    def test_iter(self):
        self.assertEqual(pow_iter(5, 5), 3125)


if __name__ == '__main__':
    unittest.main()
