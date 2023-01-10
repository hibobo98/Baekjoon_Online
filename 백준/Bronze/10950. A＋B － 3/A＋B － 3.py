import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a = map(int, sys.stdin.readline().rstrip().split())
    print(sum(a))