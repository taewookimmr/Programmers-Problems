def solution(n, cores):
    m = len(cores)
    import heapq
    heap=[]
    
    t = 1
    finished=0
    while True:
        finished = 0
        for core in cores:
            finished += t //core
        if finished >n:
            break
        t+=1 
        
    t-=1
    finished=sum([t//core for core in cores])
    accum =[t//core *core for core in cores]
    for i in range(m):
        heapq.heappush(heap,[accum[i],i])
        
    while True:
        acc, i = heapq.heappop(heap)
        heapq.heappush(heap, [acc+cores[i], i])
        finished+=1
        if finished==n:
            return i+1
        
            
        
            