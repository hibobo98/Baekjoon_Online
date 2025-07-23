def solution(arr):
    for j, i in enumerate(arr):
        if (i >= 50) and  (i % 2 == 0): # 짝수 
            arr[j] = i/2
        elif (i < 50) and (i % 2 != 0): #홀수
            arr[j] = i*2
    return arr