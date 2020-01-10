import unittest


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_prime(n):
    if n == 1:
        return True
    divider = 2
    while n % divider != 0:
        divider += 1
    return divider == n


def prime_palindrome(supremum):
    result = [0] * supremum
    for i in range(supremum):
        result[i] = i
    i = supremum - 1
    while 0 < i:
        if (is_palindrome(result[i])) & (is_prime(result[i])):
            return result[i]
        i -= 1


class TestPrimePalindrome(unittest.TestCase):
    def test_small(self):
        self.assertEqual(prime_palindrome(20), 11)

    def test_big(self):
        self.assertEqual(prime_palindrome(1000), 929)

    def test_enormous(self):
        self.assertEqual(prime_palindrome(100000), 98689)


if __name__ == '__main__':
    unittest.main()
