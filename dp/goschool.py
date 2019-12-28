def in_puddles(point,puddles):
    for puddle in puddles:
        if puddle[1] == point[0] and puddle[0] == point[1]:
            return True
    return False
def solution(m, n, puddles):
    way = [[0 for _ in range(m+1)] for _ in range(n+1)] 
    way[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not in_puddles([i, j], puddles):
                if j-1 >= 1:
                    way[i][j] += way[i][j-1] 
                if i-1 >= 1: 
                    way[i][j] += way[i-1][j] 
    return way[n][m] % 1000000007

m = 4 
n = 3
puddles = [[2,2]]
result = solution(m,n,puddles)
print(result)