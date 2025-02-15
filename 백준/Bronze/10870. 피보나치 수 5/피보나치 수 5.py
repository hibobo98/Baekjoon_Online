# 백준 10870 피보나치 수 5
def sol(n):
    if n < 2:
        return n
    return sol(n-1) + sol(n-2)

print(sol(int(input())))