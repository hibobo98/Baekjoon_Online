# 문제 1. 2961 도영이가 만든 맛있는 음식

def recur(idx, sin, ssun, use):
    global answer
    #재료=0 
    if idx == n:
        if use > 0:
            gap = abs(sin-ssun)
            answer = min(answer, gap)
        return
        
    
    #사용 
    recur(idx+1, sin*ingred[idx][0], ssun+ingred[idx][1], use+1)
    #미사용
    recur(idx+1, sin, ssun, use)
        
n = int(input())
ingred = [list(map(int,input().split())) for _ in range(n)]
answer = 1e9
recur(0,1,0,0)
print(answer)