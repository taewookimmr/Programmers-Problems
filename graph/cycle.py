def solution(n, src):
    g = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for n1,n2 in src:
        g[n1][n2]=1
    
    nowvisit = [0 for _ in range(n+1)]
    check = [0 for _ in range(n+1)]

    # 방향 그래프에서 싸이클을 확인
    def dfs(u):
        if nowvisit[u]: 
            return 1
        if  check[u] : 
            return 0

        check[u] =1
        nowvisit[u] = 1
        for i, connected in enumerate(g[u]):
            if connected:
                if dfs(i) :
                    return 1
        nowvisit[u]=0
        return 0
                     
    for i in range(1, n+1):
        nowvisit = [0 for _ in range(n+1)]
        check = [0 for _ in range(n+1)]
        print(dfs(i))


def room(arrows):
    dir = {0:[0,1],1:[1,1],2:[1,0],3:[1,-1],4:[0,-1],5:[-1,-1],6:[-1,0],7:[-1,1]}
    stack =[]
    stack.append([0,0])
    for dx,dy in arrows:
        x,y =stack[-1]
        stack.append([x+dx, y+dy])
    answer = 0
    return answer 

n = 4
graph= [[1,2], [2,3], [3,4], [4,2]]
solution(n, graph)