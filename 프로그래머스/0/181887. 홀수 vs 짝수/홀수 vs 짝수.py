def solution(num_list):
    answer = 0 
    answer2 = 0 
    for i in range(0, len(num_list), 2): # 짝수
        answer += num_list[i]
    for j in range(1, len(num_list), 2): # 홀수
        answer2 += num_list[j]
        
    answer3 = [answer, answer2]
    
    return max(answer3)