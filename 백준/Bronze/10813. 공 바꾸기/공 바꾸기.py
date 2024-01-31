M, N = map(int,input().split())
b = [i+1 for i in range(M)]
for _ in range(N):
    i, j = map(int, input().split())
    b[i-1], b[j-1] = b[j-1], b[i-1]
    
for bb in b:
    print(bb, end=' ')