def solution(N, road, K):
    MAX = 10000000
    graph = [[MAX for _ in range(N+1)] for _ in range(N+1)]
                
    for i in range(1, N+1):
        graph[i][i] = 0
        
    for connection in road:
        n1 = connection[0]
        n2 = connection[1]
        w = connection[2]
        if graph[n1][n2] > w:
            graph[n1][n2] = w
            graph[n2][n1] = w

    distance = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    
    for x in range(1, N+1):
        for y in range(1, N+1):
            distance[x][y] = graph[x][y]
            
    for x in range(1, N+1):
        for y in range(1, N+1):
            for i in range(1, N+1):
                distance[x][i] = min(distance[x][i], distance[x][y] + distance[y][i])
    return sum([1 if e <= K else 0 for e in distance[1]])
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
n = solution(N, road, K)
print(n)