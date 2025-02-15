def solution(my_string):
    answer = [0]*52
    for i in my_string:
        if i.isupper(): # 대문자 이면 65 , 소문자  97
            answer[ord(i)-65]+=1
        else:
            answer[ord(i)-71]+=1
    return answer