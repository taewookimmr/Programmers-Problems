def solution(n, works):
    if sum(works) <=n :
        return 0

    import heapq
    works=[-1*e for e in works]
    heapq.heapify(works)
    for _ in range(n):
        a = heapq.heappop(works)
        heapq.heappush(works, a+1)
    return sum([e**2 for e in works])

works = [5,4,3,2]
n = 10
result = solution(n, works)
print(result)