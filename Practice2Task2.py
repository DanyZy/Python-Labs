numders = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9}


def hidden_numbers(s):
    answer = []
    for i in s:
        try:
            answer.append(int(i))
        except ValueError:
            if i in numders:
                answer.append(numders.get(i))
    return answer


cases = [("abcdefghik", [0, 1, 2, 3, 4, 5, 6, 7, 8]),
         ("Xa,}A#5N}{xOBwYBHIlH,#W", [0, 5]),
         ("(ABW>'yy^'M{X-K}q,", []),
         ("6240488", [6, 2, 4, 0, 4, 8, 8])]
for case in cases:
    res = hidden_numbers(case[0])
    print("Expected: {}. Got: {}. Input: {}. Assert: {}".format(case[1], res, case[0], res == case[1]))
