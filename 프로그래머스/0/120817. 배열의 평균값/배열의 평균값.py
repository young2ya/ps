def solution(numbers):
    s = 0
    for i in range(len(numbers)):
        s = s + numbers[i]
    
    answer = s/len(numbers)
    return answer