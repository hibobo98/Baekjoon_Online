def solution(numbers, n):
    answer = 0
    for m in numbers:
        answer += m
        
        if answer > n:
            return answer