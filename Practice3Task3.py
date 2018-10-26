import unittest


def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def calc(expr):
    acc = []
    if expr != "":
        expr = expr.split(" ")
        for el in expr:
            if el.isdigit() or isfloat(el):
                acc.append(float(el))
            else:
                if el is "+":
                    number = acc[-2] + acc[-1]
                    acc.remove(acc[-1])
                    acc.remove(acc[-1])
                    acc.append(number)
                elif el is "-":
                    number = acc[-2] - acc[-1]
                    acc.remove(acc[-1])
                    acc.remove(acc[-1])
                    acc.append(number)
                elif el is "*":
                    number = acc[-2] * acc[-1]
                    acc.remove(acc[-1])
                    acc.remove(acc[-1])
                    acc.append(number)
                else:
                    number = acc[-2] / acc[-1]
                    acc.remove(acc[-1])
                    acc.remove(acc[-1])
                    acc.append(number)
        return acc[-1]
    else:
        return 0.0


class TestCalc(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(calc(""), 0.0)

    def test_number(self):
        self.assertEqual(calc("1 2 3"), 3.0)
        self.assertEqual(calc("0 1 1 1 1 3.5"), 3.5)

    def test_plus(self):
        self.assertEqual(calc("1 3 +"), 4.0)

    def test_mul(self):
        self.assertEqual(calc("2 5 *"), 10.0)

    def test_sub(self):
        self.assertEqual(calc("3 13 -"), -10.0)

    def test_div(self):
        self.assertEqual(calc("3 2 /"), 1.5)

    def test_hard(self):
        self.assertEqual(calc("5 1 2 + 4 * + 3 -"), 14)


if __name__ == '__main__':
    unittest.main()
