def solution(money):
    if money < 5500:
        answer = [0, money]
    else:
        coffee = money // 5500
        rest = money - coffee * 5500
        answer = [coffee, rest]
    return answer