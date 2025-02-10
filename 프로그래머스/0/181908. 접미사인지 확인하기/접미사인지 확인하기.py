def solution(my_string, is_suffix):
    ss = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in ss:
        return 1
    else:
        return 0