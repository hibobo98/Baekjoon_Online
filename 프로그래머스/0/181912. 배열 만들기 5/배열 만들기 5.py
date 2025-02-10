def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        ss = int(i[s:s+l])
        if ss > k:
            answer.append(ss)
    
    return answer