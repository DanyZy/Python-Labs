import unittest


class Seq:
    """Инициализация последовательности"""
    def __init__(self, *el):
        def seq(*elements):
            def first(x):
                return x[0]

            def other(x):
                return x[1:]

            if len(elements) == 0:
                return None
            if len(elements) == 1:
                return first(elements), None
            if len(elements) == 2:
                return first(elements), other(elements)
            return first(elements), seq(*other(elements))
        self.sequence = seq(*el)
        self.size = self.seq_size()

    """Первый элемент последовательности"""
    def head(self):
        if self.sequence is None:
            return None
        return self.sequence[0]

    """Хвост последовательности"""
    def tail(self):
        if self.sequence is None:
            return None
        if len(self.sequence) < 2:
            return None
        self.sequence = self.sequence[1]
        self.size = self.seq_size()
        return self

# Easy
    """Размер последовательности"""
    def seq_size(self):
        def rec(s, n=0):
            if s is None:
                return n
            if len(s) < 2:
                return n + 1
            return rec(s[1], n + 1)
        return rec(self.sequence)

    """Поиск элемента последовательности по индексу"""
    def at(self, index):
        def find(s, i):
            if i == 0:
                return s[0]
            return find(s[1], i - 1)
        if self.size < index:
            return None
        return find(self.sequence, index)

    """Сравнение массивов"""
    def __eq__(self, other):
        def comparison(s, o, size):
            if s[0] == o[0]:
                if size > 1:
                    return comparison(s[1], o[1], size - 1)
                return s[0] == o[0]
            return False
        if self.size != other.size:
            return False
        if self.size == 0 and other.size == 0:
            return True
        return comparison(self.sequence, other.sequence, self.size)

# Moderate
    """Хвост последовательности с пропуском значений"""
    def tail_skip(self, drop=0):
        def skip(s, d):
            if d == 0:
                return s
            return skip(s[1], d - 1)
        if self.sequence is None:
            return None
        if len(self.sequence) < 2:
            return None
        if drop == self.size:
            return None
        self.sequence = skip(self.sequence, drop)
        self.size = self.seq_size()
        return self

    """Соединение массивов"""
    def concat(self, other):
        def connect(s, o, size_s, size_o):
            if size_s > 1:
                return s[0], connect(s[1], o, size_s - 1, size_o)
            if size_s == 1:
                return s[0], connect(s, o, size_s - 1, size_o)
            if size_o > 1:
                return o[0], connect(s, o[1], size_s, size_o - 1)
            if size_o == 1:
                return o[0], None
            return None
        if self.size == 0:
            return other
        if other.size == 0:
            return self
        self.sequence = connect(self.sequence, other.sequence, self.size, other.size)
        self.size = self.seq_size()
        return self

    """Метод обхода"""
    def for_each(self, func):
        def transformation(s, size, f):
            if size == 0:
                return None
            if size == 1:
                return f(s[0]), None
            if size > 1:
                return f(s[0]), transformation(s[1], size - 1, f)
        self.sequence = transformation(self.sequence, self.size, func)
        self.size = self.seq_size()
        return self

    """Метод обхода с индексацией"""
    def for_each_index(self, func):
        def transformation(s, size, f, i=0):
            if size == 0:
                return None
            if size == 1:
                return f(i, s[0]), None
            if size > 1:
                return f(i, s[0]), transformation(s[1], size - 1, f, i + 1)
        self.sequence = transformation(self.sequence, self.size, func)
        self.size = self.seq_size()
        return self

# Hard
    """Метод преобразования"""
    def map(self, func):
        def mapping(s, size, f):
            if size == 0:
                return None
            if size > 1:
                return f(s[0]), mapping(s[1], size-1, f)
            if size == 1:
                return f(s[0]), None
        self.sequence = mapping(self.sequence, self.size, func)
        return self

    """Метод фильтрации"""
    def filter(self, func):
        def filtration(s, size, f):
            if size == 0:
                return None
            if size == 1 and f(s[0]):
                return s[0], None
            if size == 1 and not f(s[0]):
                return None
            if size > 1 and f(s[0]):
                return s[0], filtration(s[1], size - 1, f)
            return filtration(s[1], size - 1, f)
        self.sequence = filtration(self.sequence, self.size, func)
        self.size = self.seq_size()
        return self

    """Метод редуцирования"""
    def reduce(self, init_value, func):
        def transformation(s, size, i, f):
            if size == 0:
                return init_value
            if size == 1:
                return f(s[0], i)
            if size > 1:
                return f(s[0], transformation(s[1], size - 1, i, f))
        return transformation(self.sequence, self.size, init_value, func)

    """Конвертация в список"""
    def list(self):
        def convert(s, size, result):
            if size == 0:
                return []
            if size == 1:
                result.append(s[0])
                return result
            if size > 1:
                result.append(s[0])
                return convert(s[1], size - 1, result)
        return convert(self.sequence, self.size, [])


Seq(1, 2, 3, 4).for_each(lambda x: print(x))
Seq(1, 2, 3, 4).for_each_index(lambda i, x: print(i, x))


class TestSeq(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(Seq(), Seq())

    def test_at(self):
        self.assertEqual(Seq().at(1), None)
        self.assertEqual(Seq(1, 2, 3).at(2), 3)
        self.assertEqual(Seq(11, 24, 30).at(1), 24)

    def test_size(self):
        self.assertEqual(Seq().seq_size(), 0)
        self.assertEqual(Seq(1, 2).seq_size(), 2)
        self.assertEqual(Seq(1, 2, 3, 4, 5).seq_size(), 5)

    def test_eq(self):
        self.assertTrue(Seq() == Seq())
        self.assertTrue(Seq(1, 2, 3) == Seq(1, 2, 3))
        self.assertTrue(Seq(13, 9, 17, 38) == Seq(13, 9, 17, 38))
        self.assertFalse(Seq(15, 18, 24, 99) == Seq(14, 22, 83, 11))

    def test_tail(self):
        self.assertEqual(Seq(-1, -2, -3).tail(), Seq(-2, -3))
        self.assertEqual(Seq(1, 2, 3).tail_skip(3), None)
        self.assertEqual(Seq(11, 22, 33).tail_skip(2), Seq(33))

    def test_concat(self):
        self.assertEqual(Seq().concat(Seq(1, 2, 3)), Seq(1, 2, 3))
        self.assertEqual(Seq(1, 2, 3).concat(Seq()), Seq(1, 2, 3))
        self.assertEqual(Seq(1, 2, 3).concat(Seq(4, 5, 6)), Seq(1, 2, 3, 4, 5, 6))

    def test_map(self):
        self.assertEqual(Seq().map(lambda x: x ** 2), Seq())
        self.assertEqual(Seq(1, 2, 3).map(lambda x: x ** 2), Seq(1, 4, 9))
        self.assertEqual(Seq(4, 3, 2).map(lambda x: x ** 3), Seq(64, 27, 8))

    def test_filter(self):
        self.assertEqual(Seq().filter(lambda x: x * 1 == x), Seq())
        self.assertEqual(Seq(1, 2, 3, 4).filter(lambda x: x % 2 == 1), Seq(1, 3))
        self.assertEqual(Seq(1, 2, 3, 4, 5, 6).filter(lambda x: x ** 2 < 10), Seq(1, 2, 3))

    def test_reduce(self):
        self.assertEqual(Seq().reduce(1, lambda acc, cur: acc + cur), 1)
        self.assertEqual(Seq(1, 2, 3).reduce(0, lambda acc, cur: acc + cur), 6)
        self.assertEqual(Seq(1, 2, 3, 4).reduce(1, lambda acc, cur: acc * cur), 24)

    def test_list(self):
        self.assertEqual(Seq().list(), [])
        self.assertEqual(Seq(1, 2, 3, 4).list(), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()

