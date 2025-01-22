def solution(code):
    answer = ''
    mode = 0 
    for i, n in enumerate(code):
        if mode == 0:
            if n == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    answer += code[i]
        else:
            if n == "1":
                mode = 0
            else:
                if i % 2 != 0:
                    answer += code[i]
    if not answer :
        return "EMPTY"
    return answer