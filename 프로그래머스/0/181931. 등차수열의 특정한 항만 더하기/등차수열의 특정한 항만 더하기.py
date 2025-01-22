def solution(a, d, included):
    l = []
    answer = 0
    for i in range(len(included)): 
        l.append(a+i*d)
    for idx, j in enumerate(included):
        if j == True:
            answer += l[idx]
            
    return answer