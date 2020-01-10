import unittest
from Practice02.MaxPrimePalindrome import is_prime
from Practice02.SumOfDigits import summa


def filtered_accumulate(combiner, initial_value, predicate, f, start, stop, step):
    if start <= stop:
        if predicate(start):
            return combiner(initial_value, filtered_accumulate(combiner, f(start), predicate, f, step(start), stop, step))
        return filtered_accumulate(combiner, initial_value, predicate, f, step(start), stop, step)
    return initial_value


class TestFilteredAccumulate(unittest.TestCase):
    def test_1(self):
        self.assertEqual(filtered_accumulate(lambda acc, cur: acc + cur, 10,
                                             lambda x: x % 10 == 6,
                                             lambda x: x, 1, 1025, lambda i: i * 2), 10 + 16 + 256)

    def test_2(self):
        self.assertEqual(filtered_accumulate(lambda acc, cur: acc + cur, 0,
                                             lambda x: is_prime(x),
                                             lambda x: x ** 2, 0, 5, lambda i: i + 1), 1 + 4 + 9 + 25)

    def test_3(self):
        self.assertEqual(filtered_accumulate(lambda acc, cur: acc + cur, 0,
                                             lambda x: is_prime(x),
                                             lambda x: x ** 2, 0, 1, lambda i: i + 1), 1)

    def test_sum_ixi(self):
        self.assertEqual(filtered_accumulate(lambda acc, cur: acc * cur, 1,
                                             lambda n: True, lambda x: summa(x ** 2), 1, 5,
                                             lambda i: i + 1), 1 * 4 * 9 * 7 * 7)


if __name__ == '__main__':
    unittest.main()
