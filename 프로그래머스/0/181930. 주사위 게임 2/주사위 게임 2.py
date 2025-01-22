def solution(a, b, c):
    l = [a,b,c]
    if len(set(l)) == 1:
        answer = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
        
    elif len(set(l)) == 2:
        answer = (a+b+c) * (a**2+b**2+c**2)    
    else:
        answer = (a+b+c)
    
    return answer