import sys


while True:
    try:
        A, B = sys.stdin.readline().rstrip().split()
        A = int(A)
        B = int(B)
        print(int(A)+int(B))
    
    except ValueError as e:
        break