import copy
def my_solution(triangle):
    temp = copy.deepcopy(triangle)
    n = len(triangle)
    for i in range(n-1):
        for j in range(len(triangle[i])):
            if temp[i+1][j] < triangle[i+1][j] + temp[i][j]:
                temp[i+1][j]   = triangle[i+1][j] + temp[i][j]
            if temp[i+1][j+1] < triangle[i+1][j+1] + temp[i][j]:
                temp[i+1][j+1] = triangle[i+1][j+1]+ temp[i][j]      

    return max(temp[n-1])

def solution(t, l=[]):
    for r in t:
        l = [max(t,y)+z for t,y,z, in zip([0]+l,l+[0],r)]
        print(l)
    return max(l)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = solution(triangle)
print(result)