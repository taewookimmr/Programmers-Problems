def solution_slow(n,e):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    inf = 50000
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = inf
            if i==j :
                graph[i][j]=0

    for v in e:
        graph[v[0]][v[1]] = 1
        graph[v[1]][v[0]] = 1

    for i in range(1,n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if graph[x][y] > graph[x][i]+graph[i][y]:
                    graph[x][y] = graph[x][i]+graph[i][y]

    distance = graph[1]
    maxim=max(distance)
    return sum([1 if e == maxim else 0 for e in distance])    

def solution_old(n, e):
    dp = [0]*(n+1)
    g=[[] for i in range(len(e)+1)]
    
    for i in range(len(e)):
        if not e[i][1] in g[e[i][0]]:
            g[e[i][0]].append(e[i][1])
            g[e[i][0]].sort()
        if not e[i][0] in g[e[i][1]]:
            g[e[i][1]].append(e[i][0])
            g[e[i][1]].sort()
    dp[0],dp[1]= -1,-1
    queue=[1]
    count=1
    while not all(dp):
        temp=[]
        for start in queue:
            for i in g[start]:
                if dp[i] ==0:
                    dp[i]+=count
                    temp.append(i)
        queue=temp
        count+=1
    ans=dp.count(max(dp))
    return ans

def solution(n,e):
    graph = {}
    for v in e:
        for i in [0,1]:
            if v[i] in graph.keys():
                graph[v[i]].append(v[1-i])
            else : 
                graph[v[i]]= [v[1-i]]

    queue= []
    queue.append([1,0])
    check=[0 for _ in range(n+1)]
    distance = -1
    check[1]=1
    answer = []
    while len(queue):
        node, distance = queue.pop(0)
        answer.append(distance)
        for neighbor in graph[node]:
            if check[neighbor] == 0:
                queue.append([neighbor, distance+1])
                check[neighbor]=1
    print(answer)
    return answer.count(max(answer))



n= 6
e=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, e))