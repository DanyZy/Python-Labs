import unittest
import re


def compressed_sequence(sentence):
    if sentence == "":
        return sentence
    else:
        amount = {}
        result = []
        sentence = re.split('\s', sentence)
        for elem in sentence:
            amount[elem] = (amount.get(elem) or 0) + 1
        counter = list(amount.items())
        for elem in counter:
            result.append(str(elem[1]))
            result.append(elem[0])
        result = " ".join(result)
        str(result)
        return result


class TestCompressedSequence(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(compressed_sequence(""), "")

    def test_small(self):
        self.assertEqual(compressed_sequence("7"), "1 7")

    def test_small2(self):
        self.assertEqual(compressed_sequence("10 10 20"), "2 10 1 20")

    def test1(self):
        self.assertEqual(compressed_sequence(
            "40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86"
        ), "4 40 8 29 2 57 5 92 10 86")

    def test2(self):
        self.assertEqual(compressed_sequence(
            "1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 20"
        ), "2 1 3 3 4 2 3 14 3 11 1 20")

    def test3(self):
        self.assertEqual(compressed_sequence(
            "1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 20"
        ), "2 1 3 3 4 2 3 14 3 11 1 20")


if __name__ == '__main__':
    unittest.main()
