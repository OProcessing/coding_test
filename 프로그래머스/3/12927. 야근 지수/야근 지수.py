def solution(n, works):
    while n > 0 : 
        works.sort(reverse=True)
        if works[0] > 0 :
            for j in range(works.count(max(works))) :
                if n > 0 :
                    works[j] -= 1
                    n -= 1
                else : break
        else : break
    works = [x**2 for x in works]
    return sum(works)