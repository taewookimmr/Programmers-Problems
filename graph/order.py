def solution_old(n, results):
    forward = [[0 for _ in range(n+1)] for _ in range(n+1)]
    backward = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for r in results:
        win=r[0]
        lose=r[1]
        forward[lose][win] = 1
        backward[win][lose] = 1
    
    ahead, back = [],[]
    # 시작 노드에서 forward로 나아갔을때 몇 놈이 앞에 있는지
    for i in range(1, n+1):
        queue = []
        count = 0
        queue.append(i)
        check=[0 for _ in range(n+1)]
        check[i]=1
        while len(queue):
            node = queue.pop(0)
            for j in range(1,n+1):
                if forward[node][j]:
                    if check[j]==0:
                        check[j]=1
                        queue.append(j)
        ahead.append(sum(check)-1)
    # 시작 노드에서 bacward 나아갔을때 몇 놈이 뒤에 있는지        
    for i in range(1, n+1):
        queue = []
        count = 0
        queue.append(i)
        check=[0 for _ in range(n+1)]
        check[i]=1
        while len(queue):
            node = queue.pop(0)
            for j in range(1,n+1):
                if backward[node][j]:
                    if check[j]==0:
                        check[j]=1
                        queue.append(j)
        back.append(sum(check)-1)
    
    # print(ahead, back)
    return sum([1 if e+a==n-1 else 0 for e,a in zip(ahead, back)])



def solution(n, results):  
    forward = [[0 for _ in range(n+1)] for _ in range(n+1)]
    backward = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for win, lose in results:
        forward[lose][win] = 1
        backward[win][lose] = 1
    
    ahead, back = [],[]
    def kakaotexi(graph, dst):
        for i in range(1, n+1):
            queue = []
            count = 0
            queue.append(i)
            check=[0 for _ in range(n+1)]
            check[i]=1
            while len(queue):
                node = queue.pop(0)
                for j in range(1,n+1):
                    if graph[node][j]:
                        if check[j]==0:
                            check[j]=1
                            queue.append(j)
            dst.append(sum(check)-1)

    kakaotexi(forward,ahead)
    kakaotexi(backward,back)

    return sum([1 if e+a==n-1 else 0 for e,a in zip(ahead, back)]) 