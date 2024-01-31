H,M = map(int,input().split())
T = int(input())

if (M + T) >= 60:
    C = (M + T) //  60
    M = (M + T) - 60*C
    H += C
    if H >= 24:
        H -= 24
else:
    M += T 


print(H, M)