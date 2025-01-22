def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
        
    b = sum(num_list)
    if answer > b**2 :
        return 0 
    else:
        return 1