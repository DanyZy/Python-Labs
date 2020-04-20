# TODO: реализовать тип данных множество на основе хеш-таблицы
import unittest


size_table = 10
fun = lambda f, x: abs(f(x)) % size_table


class Set:
    def __init__(self, elements, f):
        self.arr = []
        for i in range(size_table):
            self.arr.append([])
        for num in elements:
            self.add(num, f)

    def add(self, x, f):
        if not self.__contains__(x, f):
            self.arr[fun(f, x)].append(x)

    def __contains__(self, x, f):
        exist = False
        for i in self.arr[fun(f, x)]:
            exist = exist or (i == x)
        return exist


class TestSet(unittest.TestCase):

    def test_set(self):
        self.assertTrue(Set([1, 2, 3, 3], lambda x: x) == Set((1, 2, 3), lambda x: x))


if __name__ == '__main__':
    unittest.main()
