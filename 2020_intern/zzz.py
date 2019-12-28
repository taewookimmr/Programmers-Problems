import sys
sys.setrecursionlimit(10**6)

def solution(land, height):
    alldir = [[-1,0],[0,-1],[1,0],[0,1]]
    rightdown=[[1,0],[0,1]]
    n = len(land)
    dp = [[n*n for _ in range(n)] for _ in range(n)]
    check=[[0 for _ in range(n)] for _ in range(n)]

    def grouping(r,c, seed):
        if dp[r][c]<seed:
            return
        dp[r][c]=seed
        check[r][c]=1
        for dr,dc in alldir:
            rr=r+dr
            cc=c+dc
            if  rr>=0 and rr<n and cc>=0 and cc<n and check[rr][cc]==0: # out of bound check
                if abs(land[r][c]-land[rr][cc]) <= height: # group check
                    grouping(rr,cc,seed) 
    V=0
    for i in range(n):
        for j in range(n):
            if check[i][j]==0:
                grouping(i,j,V)
                V+=1
        
#   여기까지는 시간초과 안남               
#   V는 노드의 개수
#   노드가 하나 밖에 없으면 사다리를 놓을 필요가 없다.

    if V==1:
        return 0

    edge={}
    def graphing(r,c):
        for dr,dc in rightdown:
            rr=r+dr
            cc=c+dc
            if  rr>=0 and rr<n and cc>=0 and cc<n: # out of bound check
                    dist= abs(land[r][c]-land[rr][cc])
                    if dist > height and dp[r][c]!=dp[rr][cc]: # group check
                        v1=dp[r][c]
                        v2=dp[rr][cc]
                        if v1>v2:
                            v1,v2=v2,v1          
                        k=str(v1)+str(v2)
                        if k in edge.keys():
                            edge[k][0] = min(edge[k][2], dist)
                        else :
                            edge[k]=[dist,v1,v2]

    for i in range(n-1): ## 마지막 열은 검사받기만 하면 되기 때문에 n-1
        for j in range(n):
        	graphing(i,j)
    
    E= len(edge)
    edge=list(edge.values())
    
    if V==2:
        return edge[0][0]
    
#   이 위에서 graphing이 완료된다.  ----------------------------------- -----------------------------------
#   mcst를 구하고 그 길이를 반환하면 됩니다.
#   kruskal을 사용하도록 합시다.

    parent = {}
    rank = {}
    
    graph={}
    graph['vertices'] = [e for e in range(V)]
    graph['edges']= edge
    # 정점을 독립적인 집합으로 만든다.
    def make_set(v):
        parent[v] = v
        rank[v] = 0
    
    # 해당 정점의 최상위 정점을 찾는다.
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])

        return parent[v]
    
    # 두 정점을 연결한다.
    def union(v, u):
        root1 = find(v)
        root2 = find(u)

        if root1 != root2:
            # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2

                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    def kruskal(graph):    
        for v in graph['vertices']:
            make_set(v)

        mst = []

        edges = graph['edges']
        edges.sort()

        for edge in edges:
            weight, v, u = edge

            if find(v) != find(u):
                union(v, u)
                mst.append(edge)

        return sum([e[0] for e in mst])
    
	return kruskal(graph)