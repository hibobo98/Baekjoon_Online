def solution(start_num, end_num):
    answer = [i for i in range(end_num, start_num+1)]
    answer.sort(reverse=True)
    return answer