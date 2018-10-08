import re
from operator import itemgetter


def word_count(sentence):

    sentence = re.split('\s', sentence)
    freq = {}

    for word in sentence:
        if len(word) < 2:
            continue
        else:
            freq[word] = (freq.get(word) or 0) + 1
    freq_list = list(freq.items())
    freq_list.sort(key=itemgetter(1), reverse=True)
    result = []
    max_len = 10
    if len(freq_list) < max_len:
        max_len = len(freq_list)
    for i in range(0, max_len):
        result.append(freq_list[i][0])
    return result


cases = [("aa aa aa bb cc cc A B C a AA", ["aa", "cc", "bb", "AA"]), ("", [])]
for case in cases:
    res = word_count(case[0])
    print("Expected: {}. Got: {}. Input: {}. Assert: {}".format(case[1], res, case[0], res == case[1]))