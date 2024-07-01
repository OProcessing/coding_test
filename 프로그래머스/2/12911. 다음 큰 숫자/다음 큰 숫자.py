def solution(n):
    n_bin = format(n, 'b').count('1')
    for k in range(n+1, n*2+1) :
        k_bin = format(k, 'b').count('1')
        if n_bin == k_bin : 
            return k