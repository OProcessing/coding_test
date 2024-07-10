def solution(brown, yellow):
    s = brown + yellow
    for i in range(s, 0, -1) :
        if s % i == 0 :
            temp = int(s/i)
            if (i * 2 + (temp - 2) * 2) == brown :
                return([i, temp])
        else : pass
    
    