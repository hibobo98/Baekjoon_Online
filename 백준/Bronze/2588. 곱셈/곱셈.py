A = int(input())
B = int(input())
one = B//100
two = (B - one*100)//10
three = B - (one*100 + two*10)
print(A * three)
print(A* two)
print(A*one)
print(A*B)