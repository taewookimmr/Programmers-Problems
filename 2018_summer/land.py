def solution(land, P, Q):

    land_1d = []
    for row in land:
        land_1d += row
    land_1d.sort()
    maxh = land_1d[-1]
    minh = land_1d[0]    

    def func(t):
        return sum([(t-c)*P if t-c >= 0 else (c-t)*Q for c in land_1d])

    answer = []
    import heapq

    left = minh
    right = maxh
    x = (left+right)//2
    while left < right:
        if func(x) < func(x+1) :
            right = x
        else :
            left = x+1
        x = (left+right)//2
    heapq.heappush(answer, func(x)) 

    return heapq.heappop(answer)
land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
n = solution(land, 5, 3)                    
print(n)