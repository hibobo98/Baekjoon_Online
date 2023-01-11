import sys
X = sys.stdin.readline().rstrip()
N = sys.stdin.readline().rstrip()
l = []
# a, b = sys.stdin.readline().rstrip().split()


X = int(X)
for i in range(int(N)):
    a, b = sys.stdin.readline().rstrip().split()
    X -= int(a)*int(b)
print("Yes" if X == 0 else "No")