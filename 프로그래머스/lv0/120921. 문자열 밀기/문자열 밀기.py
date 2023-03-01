def solution(A, B):
    i = 0
    length = len(A)
    if A == B:
        return 0
    for _ in range(length):
        new = A[-1] + A[:-1]
        i += 1
        A = new
        if A == B:
            chance = i
            return chance
        answer = -1
    return answer