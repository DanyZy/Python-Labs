import timeit

declare = lambda x: 'Set size: ' + str(x) + ', Time: '
init = 'import random\n' \
       'from BSTBasedSet import Tree, Set\n'

print('Add Set')

action = 'for num in lst: a.add(num)'
strlst = lambda x: 'a = Set()\nlst = [random.randint(1, 500) for r in range(' + str(x) + ')]'

print(declare(10), timeit.timeit(action, setup=init + strlst(10), number=10))
print(declare(50), timeit.timeit(action, setup=init + strlst(50), number=10))
print(declare(100), timeit.timeit(action, setup=init + strlst(100), number=10), '\n')

print('Union Set')

action = 's1 + s2'
strset = lambda x, y: x + ' = Set()\nfor num in [random.randint(1, 500) for r in range(' + str(y) + ')]: ' + x + '.add(num)'

print(declare(10), timeit.timeit(action, setup=init+strset('s1', 5)+'\n'+strset('s2', 5), number=10))
print(declare(50), timeit.timeit(action, setup=init+strset('s1', 25)+'\n'+strset('s2', 25), number=10))
print(declare(100), timeit.timeit(action, setup=init+strset('s1', 50)+'\n'+strset('s2', 50), number=10), '\n')

print('Intersection Set')

action = 's1 * s2'

print(declare(10), timeit.timeit(action, setup=init+strset('s1', 10)+'\n'+strset('s2', 20), number=10))
print(declare(50), timeit.timeit(action, setup=init+strset('s1', 50)+'\n'+strset('s2', 50), number=10))
print(declare(100), timeit.timeit(action, setup=init+strset('s1', 100)+'\n'+strset('s2', 100), number=10), '\n')

print('Set Contains')

action = 'element in s'
elem = 'element = random.randint(1, 500)'

print(declare(10), timeit.timeit(action, setup=init + strset('s', 10)+'\n'+elem, number=100))
print(declare(50), timeit.timeit(action, setup=init + strset('s', 50)+'\n'+elem, number=100))
print(declare(100), timeit.timeit(action, setup=init + strset('s', 100)+'\n'+elem, number=100), '\n')
