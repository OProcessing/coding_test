def solution(x):
    x4 = (x // 1000)
    x3 = (x // 100) % 10
    x2 = (x // 10) % 10
    x1 = x % 10
    
    if (x % (x1 + x2 + x3 + x4)) : return False
    return True