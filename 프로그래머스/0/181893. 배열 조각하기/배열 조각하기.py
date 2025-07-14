def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i % 2 != 0: # 홀수 
            arr = arr[query[i]:]
        else: # 짝수
            arr = arr[:query[i]+1]
    return arr