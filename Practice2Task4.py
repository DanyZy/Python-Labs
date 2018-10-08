# encoding: utf-8
import unittest
from math import sqrt
from itertools import count, islice


def is_palindrome(n):
    number = str(n)
    reverse = number[::-1]
    if number == reverse:
        return True
    else:
        return False


def is_prime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n % number:
            return False
    return True


def prime_palindrome(supremum):
    result = [0] * supremum
    for i in range(supremum):
        result[i] = i
    i = supremum - 1
    while 0 < i:
        if (is_palindrome(result[i])) & (is_prime(result[i])):
            return result[i]
        i -= 1


# Тут тесты
class TestPrimePalindrome(unittest.TestCase):
    def test_small(self):
        self.assertEqual(prime_palindrome(20), 11)

    def test_big(self):
        self.assertEqual(prime_palindrome(1000), 929)

    def test_enormous(self):
        self.assertEqual(prime_palindrome(100000), 98689)


if __name__ == '__main__':
    unittest.main()
