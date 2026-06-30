def solution(n, k):
    cost = 12000 * n + 2000 * k
    if n // 10 >= 0:
        service = n // 10
        
        cost = cost - service * 2000
        
    return cost