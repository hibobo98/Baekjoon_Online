import sys

N = sys.stdin.readline().rstrip()
N = int(N)
num = N
i = 0

while True:
    one = N//10 
    two = N % 10 

    tot = one + two

    N = two * 10 + tot % 10 

    i+= 1

    if num == N:
        print(i)
        break
