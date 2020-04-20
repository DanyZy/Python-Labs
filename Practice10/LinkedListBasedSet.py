from Practice09.RecursivelyConnectedSequence import *


class Set(Seq):
    """Инициализация множества"""
    def __init__(self, *elements):
        if len(elements) == 1 and isinstance(elements[0], list):
            elements = elements[0]
        super().__init__(*elements)
        for el in elements:
            # Зависимость от метода add
            self.add(el)

    """Добавление элемнетов"""
    def add(self, element):
        return self.filter(lambda x: x != element).concat(Seq(element))

    """Объединение множеств"""
    def union(self, other):
        return Set(self.concat(other).list())

    """Проверка на вхождение элемента"""
    def __contains__(self, element):
        return self.filter(lambda x: x == element) != Set()

    """Пересечение множеств"""
    def intersection(self, other):
        # Зависимость от метода contains
        return self.filter(lambda x: x in other)


class TestSet(unittest.TestCase):

    def test_set(self):
        self.assertTrue(Set(7, 8, 9) == Set(7, 7, 8, 9))

    def test_set_from_list(self):
        self.assertEqual(Set([]), Set())
        self.assertEqual(Set([1, 2, 3]), Set(1, 2, 3))

    def test_add(self):
        self.assertEqual(Set().add(1), Seq(1))
        self.assertEqual(Set(1, 2, 3).add(4), Seq(1, 2, 3, 4))
        self.assertEqual(Set(1, 2, 3).add(3), Seq(1, 2, 3))

    def test_set_size(self):
        self.assertEqual(Set(1, 3, 6, 9, 2, 3, 9).size(), 5)
        self.assertEqual(Set(4, 6, 5, 8, 8, 4, 5).size(), 4)

    def test_list(self):
        self.assertEqual(Set().list(), [])
        self.assertEqual(Set(1, 2, 3, 4).list(), [1, 2, 3, 4])

    def test_set_contains(self):
        self.assertFalse(1 in Set())
        self.assertTrue(3 in Set(1, 2, 3, 4))

    def test_for_each(self):
        self.assertEqual(Set("a", "b").for_each(lambda x: x + "c"), Set("ac", "bc"))
        self.assertEqual(Set(1, 2, 3, 4).for_each(lambda x: x + 1), Set(2, 3, 4, 5))

    def test_union(self):
        self.assertEqual(Set().union(Set()), Set())
        self.assertEqual(Set(1, 2, 3).union(Set(4, 5)), Set(1, 2, 3, 4, 5))
        self.assertEqual(Set(1, 2, 3).union(Set(1, 2, 4, 5)), Set(3, 1, 2, 4, 5))

    def test_intersection(self):
        self.assertEqual(Set().intersection(Set(2, 3, 4)), Set())
        self.assertEqual(Set(1, 2, 3).intersection(Set(2, 3, 4)), Set(2, 3))


if __name__ == '__main__':
    unittest.main()
