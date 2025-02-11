def solution(my_string, is_prefix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[:i])
    if is_prefix in answer:
        return 1
    else:
        return 0