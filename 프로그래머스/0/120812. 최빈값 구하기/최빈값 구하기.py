from collections import Counter

def solution(array):
    c = Counter(array)
    most = c.most_common()
    if len(most) > 1 and most[0][1] == most[1][1]:
        return -1
    return most[0][0]