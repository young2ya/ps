def solution(array, height):
    array.sort()
    a = 0
    for i in array:
        if i>height:
            a += 1
    return a