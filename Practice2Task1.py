def summa(num):
    x = 0
    while num > 0:
        x += num % 10
        num //= 10
    return x


cases = [(1234, 10), (1024, 7), (0, 0), (3333, 12)]
for case in cases:
    res = summa(case[0])
    print("Expected: {}. Got: {}. Input: {}. Assert: {}".format(case[1], res, case[0], res == case[1]))
