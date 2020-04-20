import timeit

declare = lambda x: 'Set size: ' + str(x) + ', Time: '
init = 'import random\n' \
       'from LinkedListBasedSet import Set\n'

print('Create Set')

action = 'Set(lst)'
strlst = lambda x: 'lst = [random.randint(0, 100) for r in range(' + str(x) + ')]'

print(declare(10), timeit.timeit(action, setup=init + strlst(10), number=10))
print(declare(50), timeit.timeit(action, setup=init + strlst(50), number=10))
print(declare(100), timeit.timeit(action, setup=init + strlst(100), number=10), '\n')

print('Union Set')

action = 'Set.union(s1, s2)'
strset = lambda x, y: x + ' = Set([random.randint(0, 100) for r in range(' + str(y) + ')])'

print(declare(10), timeit.timeit(action, setup=init+strset('s1', 5)+'\n'+strset('s2', 5), number=10))
print(declare(50), timeit.timeit(action, setup=init+strset('s1', 25)+'\n'+strset('s2', 25), number=10))
print(declare(100), timeit.timeit(action, setup=init+strset('s1', 50)+'\n'+strset('s2', 50), number=10), '\n')

print('Intersection Set')

action = 'Set.intersection(s1, s2)'

print(declare(10), timeit.timeit(action, setup=init+strset('s1', 10)+'\n'+strset('s2', 20), number=10))
print(declare(50), timeit.timeit(action, setup=init+strset('s1', 50)+'\n'+strset('s2', 50), number=10))
print(declare(100), timeit.timeit(action, setup=init+strset('s1', 100)+'\n'+strset('s2', 100), number=10), '\n')

print('Set Contains')

action = 'Set.contains(s, element)'
elem = 'element = random.randint(0, 100)'

print(declare(10), timeit.timeit(action, setup=init + strset('s', 10)+'\n'+elem, number=100))
print(declare(50), timeit.timeit(action, setup=init + strset('s', 50)+'\n'+elem, number=100))
print(declare(100), timeit.timeit(action, setup=init + strset('s', 100)+'\n'+elem, number=100), '\n')
