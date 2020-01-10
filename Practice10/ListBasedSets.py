from Practice9.RecursivelyConnectedSequence import *


class Set:
    """Инициализация множества"""
    def __init__(self, *elements):
        if len(elements) > 0 and isinstance(elements[0], list):
            elements = elements[0]
        for i in elements:
            self.set = self.add(i)

    """Добавление элемнетов"""
    def add(self, element):
        return Seq().concat(Seq().filter(lambda x: x != element), Seq(element))

    """Конвертация в список"""
    def list(self):
        return Seq(self).list()

    def SetSize(self):
        return Seq().seq_size()

    def set_contains(self, element):
        return Seq.filter(lambda x: x == element)


class TestProcessSet(unittest.TestCase):

    def test_Set(self):
        a = Set(7, 8, 9)
        b = Set(7, 8, 9)
        self.assertTrue(a == b)

    def test_SetSize(self):
        a = Set(1, 3, 6,9,2,3,9)
        b = Set([4,6,5,8,8,4,5])
        self.assertEqual(Set(a).SetSize(), 5)
        self.assertEqual(Set(b).SetSize(), 4)


if __name__ == '__main__':
    unittest.main()
