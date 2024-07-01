def solution(triangle):
    l = len(triangle)
    for i in range(l-2, -1, -1) :
        for j in range(0, i+1) :
            cal_triangle(triangle, i, j)
    return triangle[0][0]

def cal_triangle(triangle, row, col) :
    left = triangle[row+1][col]
    right = triangle[row+1][col+1]
    if left > right : triangle[row][col] += left
    else : triangle[row][col] += right