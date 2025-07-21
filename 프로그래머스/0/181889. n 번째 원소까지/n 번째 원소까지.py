def solution(num_list, n):
    answer = []
    for m, i in enumerate(num_list):
        answer.append(i)
        if m+1 == n:
            return answer
