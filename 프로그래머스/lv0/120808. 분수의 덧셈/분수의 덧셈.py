import math 
def solution(numer1, denom1, numer2, denom2):
    one = numer1 * denom2 + numer2 * denom1
    two = denom2 * denom1
    mini = math.gcd(one, two)
    return [one//mini, two//mini]