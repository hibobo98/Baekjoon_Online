import sys
n = int(sys.stdin.readline().rstrip())
k = 0
for i in range(n+1):
    k += i
print(k)