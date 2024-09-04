import math

def solution(arr):
    result = arr[0]
    for i in arr[1:]:
        result = abs(result * i) // math.gcd(result, i)
    return result