def solution(my_strings, parts):
    answer = ''
    for k, i in enumerate(my_strings):
        s,e = parts[k]
        answer+=i[s:e+1]
    return answer