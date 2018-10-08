# encoding: utf-8
import unittest


def mixed_content(sentence):
    if sentence != "":
        numbers = []
        words = []
        sentence = sentence.split(',')
        for elem in sentence:
            if elem.isdigit():
                numbers.append(elem)
            else:
                words.append(elem)
        if not numbers:
            return ",".join(words)
        elif not words:
            return ",".join(numbers)
        else:
            return ",".join(words) + "|" + ",".join(numbers)
    else:
        return ""


class TestMixedContent(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(mixed_content(""), "")

    def test_small(self):
        self.assertEqual(mixed_content("1,apple,2"), "apple|1,2")

    def test_only_numbers(self):
        self.assertEqual(mixed_content("1,2"), "1,2")

    def test_only_words(self):
        self.assertEqual(mixed_content("bb,aa"), "bb,aa")

    def test(self):
        self.assertEqual(
            mixed_content("8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21"),
            "melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21"
        )

if __name__ == '__main__':
    unittest.main()
