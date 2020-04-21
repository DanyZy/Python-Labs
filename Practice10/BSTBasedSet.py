import unittest


class Tree:
    """Инициализация дерева"""
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    """Добавление элемента"""
    def add(self, key):
        if self.key is None:
            self.key = key
            self.left = Tree()
            self.right = Tree()
        else:
            if key > self.key:
                self.right.add(key)
            elif key < self.key:
                self.left.add(key)

    """Объединение множеств"""
    def __add__(self, that):
        result = Tree()
        f = lambda x: result.add(x)
        self.for_each(f)
        that.for_each(f)
        return result

    """Пересечение множеств"""
    def __mul__(self, that):
        result = Tree()
        self.for_each(lambda x: result.add(x) if x in that else None)
        return result

    """Проверка на вхождение элемента"""
    def __contains__(self, item):
        if self.key is None:
            return False
        elif item > self.key:
            return item in self.right
        elif item < self.key:
            return item in self.left
        return True

    """Получение длины множетва"""
    def __len__(self):
        result = 0
        def process(x):
            nonlocal result
            result += 1
        self.for_each(process)
        return result

    """Обход по элементам множества"""
    def for_each(self, fun):
        if self.key is not None:
            fun(self.key)
            self.left.for_each(fun)
            self.right.for_each(fun)

    """Конвертация в список"""
    def list(self):
        lst = []
        def process(x):
            lst.append(x)
        self.for_each(process)
        return lst


"""Инициализация множества"""
def Set(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], list):
        numbers = numbers[0]
    result = Tree()
    for i in numbers:
        result.add(i)
    return result


class TestProcessSet(unittest.TestCase):

    def test_set(self):
        Set()
        Set(1, 2, 3)

    def test_contains(self):
        self.assertTrue(1 in Set([1, 2, 3]))
        self.assertFalse(4 in Set(1, 2, 3))

    def test_add(self):
        a = Set(1, 2, 3)
        a.add(4)
        self.assertTrue(len(a) == 4 and (4 in a))

    def test_list(self):
        self.assertTrue(isinstance(Set(1, 2, 3).list(), list))
        self.assertEqual(len(Set(1, 2, 3, 3).list()), 3)

    def test_size(self):
        self.assertEqual(len(Set([1, 2, 3])), 3)
        self.assertEqual(len(Set(1, 1, 2, 2, 3, 3)), 3)

    def test_union(self):
        s1 = Set([1, 2, 3])
        s2 = Set(3, 4, 5)
        s3 = s1 + s2
        self.assertEqual(len(s3), 5)
        self.assertEqual(s3.list(), [1, 2, 3, 4, 5])

    def test_intersection(self):
        s1 = Set(1, 2, 3, 5)
        s2 = Set(3, 4, 5)
        s3 = s1 * s2
        self.assertEqual(len(s3), 2)
        self.assertEqual(s3.list(), [3, 5])

    def test_for_each(self):
        lst = []
        Set(1, 2, 3).for_each(lambda x: lst.append(x * 2))
        self.assertEqual(lst, [2, 4, 6])


if __name__ == '__main__':
    unittest.main()
