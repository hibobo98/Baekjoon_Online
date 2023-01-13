import sys

T = sys.stdin.readline().rstrip()

for i in range(int(T)):
    A, B = sys.stdin.readline().rstrip().split()
    print(f"Case #{i+1}: {A} + {B} = {int(A)+int(B)}")