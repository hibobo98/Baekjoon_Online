# def solution(arr, idx):
#     answer=[]
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             answer.append(i)
#     answer2 = [i for i in answer if i >= idx]
        
#     if len(answer2) == 0:
#         return -1
#     else:
#         return answer2[0]
        
def solution(arr, idx):
    try:
        answer = arr.index(1, idx)
        return answer
    except:
        return -1