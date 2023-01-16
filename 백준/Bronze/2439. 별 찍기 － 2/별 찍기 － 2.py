import sys

N = sys.stdin.readline().rstrip()
N= int(N)

j = 1

for i in reversed(range(N)): # 4,3,2,1,0
    print(" "*i,end = '')
    print("*"*j)
    j += 1