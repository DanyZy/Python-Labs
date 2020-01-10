import unittest


def accumulate(combiner, initial_value, f, start, stop, step):
    if start <= stop:
        return combiner(initial_value, accumulate(combiner, f(start), f, step(start), stop, step))
    return initial_value


class TestAccumulate(unittest.TestCase):
    def test_1(self):
        self.assertEqual(accumulate(lambda acc, cur: acc ** cur,
                                    2, lambda x: x + 2, 2, 5, lambda i: i + 2), 2 ** 4 ** 6)

    def test_2(self):
        result = 1 + 2 ** 2 + 3 ** 2 + 4 ** 2 + 5 ** 2 + 6 ** 2 + 7 ** 2 + 8 ** 2 + 9 ** 2 + 10 ** 2
        self.assertEqual(accumulate(lambda acc, cur: acc + cur,
                                    0, lambda x: x ** 2, 1, 10, lambda i: i + 1), result)


if __name__ == '__main__':
    unittest.main()
