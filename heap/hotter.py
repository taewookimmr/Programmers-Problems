def solution(sc, k):
    import heapq
    heapq.heapify(sc)

    count = 0
    while len(sc):
        a= heapq.heappop(sc)
        if a >= K:
            break
        else:
            count +=1 

        if len(sc):
            b = heapq.heappop(sc)
            c = a+b*2
            heapq.heappush(sc, c)
        else:
            return -1
    return count

def solution_old( scoville, k):
    import sys
    import heapq

    heap = scoville
    heapq.heapify(heap)

    loopcount = 0
    while len(heap) >= 2 and min(heap) < k  :
        loopcount+=1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap,a+b*2)
        if len(heap) == 1 and heap[0] < k:
            return -1
    

    return (loopcount)
scoville = [10,1,2,3,9,10,12]
K = 7
print(solution(scoville, K))