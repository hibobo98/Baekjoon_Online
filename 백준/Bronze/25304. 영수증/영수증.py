import sys
X = sys.stdin.readline().rstrip()
N = sys.stdin.readline().rstrip()
l = []

for i in range(int(N)):
    a, b = sys.stdin.readline().rstrip().split()
    l.append(int(a)*int(b))
s = sum(l)
if s == int(X):
    print('Yes')
else:
    print('No')