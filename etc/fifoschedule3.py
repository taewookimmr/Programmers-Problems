## heap으로 처리
def solution(n, cores):
    m = len(cores)
    heap = []
    import heapq
    for i in range(m):
        heapq.heappush(heap, [0,i])
        
    while n>0:
        acc, i = heapq.heappop(heap)
        heapq.heappush(heap, [acc+cores[i],i])
        n-=1
        if n==0:
            return i+1