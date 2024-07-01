def solution(n):
    answer = 0
    sum = 0
    for k in range(0, n) :
        sum += k
        if n > sum :
            if (n-sum) % (k+1) == 0 : 
                answer +=1
                print (n-sum, sum, k, answer)
        else : break
    return answer
    


    #k = 0 , sum = 0 , 15 % 1 == 0 /  n
    #k = 1 , sum = 1 , 14 % 2 == 0 / 2n + 1
    #k = 2 , sum = 3 , 12 % 3 == 0 / 3n + 3
    #k = 3 , sum = 6 , 09 % 4 != 0 / 4n + 6
    #k = 4 , sum = 10 , 5 % 5 == 0 / 5n + 10
    #k = 5 , sum = 15 , 0 % 6 != 0 / 6n + 15