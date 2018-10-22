import unittest


def process_tower(height):
    column1 = []
    column2 = []
    column3 = []
    columns = [column1, column2, column3]

    def filling_massive(i):
        if i > 0:
            column1.append(str(i - 1))
            return filling_massive(i - 1)
        else:
            return column1

    filling_massive(height)

    def converting_result(i, j, col):
        return str(i)+"->"+str(j)+". [["+", ".join(col[0])+"], ["+", ".join(col[1])+"], ["+", ".join(col[2])+"]]"

    def permutation(columns, height, i, j):
        if height == 1:
            columns[j].append(columns[i].pop())
            return [converting_result(i, j, columns)]
        else:
            result = permutation(columns, height - 1, i, 3 - i - j)
            result += permutation(columns, 1, i, j)
            return result + permutation(columns, height - 1, 3 - i - j, j)
    if height > 0:
        return permutation(columns, height, 0, 1)
    else:
        return []


class TestProcessTower(unittest.TestCase):
    def test_empty(self):
        self.assertListEqual(process_tower(0), [])

    def test_one_height(self):
        self.assertListEqual(process_tower(1), ["0->1. [[], [0], []]"])

    def test_three(self):
        self.assertListEqual(process_tower(3), [
            "0->1. [[2, 1], [0], []]",
            "0->2. [[2], [0], [1]]",
            "1->2. [[2], [], [1, 0]]",
            "0->1. [[], [2], [1, 0]]",
            "2->0. [[0], [2], [1]]",
            "2->1. [[0], [2, 1], []]",
            "0->1. [[], [2, 1, 0], []]"
        ])

    def test_five(self):
        operations = ['0->1. [[4, 3, 2, 1], [0], []]', '0->2. [[4, 3, 2], [0], [1]]', '1->2. [[4, 3, 2], [], [1, 0]]',
                      '0->1. [[4, 3], [2], [1, 0]]', '2->0. [[4, 3, 0], [2], [1]]', '2->1. [[4, 3, 0], [2, 1], []]',
                      '0->1. [[4, 3], [2, 1, 0], []]', '0->2. [[4], [2, 1, 0], [3]]', '1->2. [[4], [2, 1], [3, 0]]',
                      '1->0. [[4, 1], [2], [3, 0]]', '2->0. [[4, 1, 0], [2], [3]]', '1->2. [[4, 1, 0], [], [3, 2]]',
                      '0->1. [[4, 1], [0], [3, 2]]', '0->2. [[4], [0], [3, 2, 1]]', '1->2. [[4], [], [3, 2, 1, 0]]',
                      '0->1. [[], [4], [3, 2, 1, 0]]', '2->0. [[0], [4], [3, 2, 1]]', '2->1. [[0], [4, 1], [3, 2]]',
                      '0->1. [[], [4, 1, 0], [3, 2]]', '2->0. [[2], [4, 1, 0], [3]]', '1->2. [[2], [4, 1], [3, 0]]',
                      '1->0. [[2, 1], [4], [3, 0]]', '2->0. [[2, 1, 0], [4], [3]]', '2->1. [[2, 1, 0], [4, 3], []]',
                      '0->1. [[2, 1], [4, 3, 0], []]', '0->2. [[2], [4, 3, 0], [1]]', '1->2. [[2], [4, 3], [1, 0]]',
                      '0->1. [[], [4, 3, 2], [1, 0]]', '2->0. [[0], [4, 3, 2], [1]]', '2->1. [[0], [4, 3, 2, 1], []]',
                      '0->1. [[], [4, 3, 2, 1, 0], []]']
        self.assertListEqual(process_tower(5), operations)


if __name__ == '__main__':
    unittest.main()
