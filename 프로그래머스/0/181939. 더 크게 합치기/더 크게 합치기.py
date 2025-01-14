def solution(a, b):
    answer = str(a) + str(b)
    answer2 = str(b) + str(a)
    if int(answer) > int(answer2):
        a = answer
    elif int(answer) < int(answer2):
        a = answer2
    else:
        a = answer
    return int(a)