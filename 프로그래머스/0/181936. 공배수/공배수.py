def solution(number, n, m):
    if (number % n == 0) & (number % m == 0):
        answer = 1
    else:
        answer = 0
    return answer