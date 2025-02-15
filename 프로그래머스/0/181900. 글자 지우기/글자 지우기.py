def solution(my_string, indices):
    answer = ''
    my = [i for i in my_string]
    for i in sorted(indices, reverse=True):
        my.pop(i)
        
    for j in my:
        answer+=j
    return answer