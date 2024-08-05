def solution(money):
    
    case1 = [0] * len(money)
    case2 = [0] * len(money)
    
    case1[0] = money[0]
    for i in range(1, len(money)-1) :
        case1[i] = max(case1[i-1], case1[i-2] + money[i])
    
    case2[0] = 0
    for i in range(1, len(money)) :
        case2[i] = max(case2[i-1], case2[i-2] + money[i])
        
    return max(case1[-2], case2[-1])