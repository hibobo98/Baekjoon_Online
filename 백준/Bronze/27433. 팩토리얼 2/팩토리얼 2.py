def sol(n):
    if n < 2:
        return 1
    else:
        return n*sol(n-1)

print(sol(int(input())))