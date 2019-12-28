
def solution(distance, rocks, n):
    rocks.sort()
    m = len(rocks)
    answer = 1
    start = 1
    end = distance 

    while start <= end:
        mid = (start + end)//2
        cnt = 0
        last = 0
        for i in range(m+1):
            gap = rocks[i]-last if i != m else distance-rocks[i-1]
            if gap < mid:
                cnt +=1
            elif i != m:
                last = rocks[i]
        
        if cnt > n:
            end = mid -1
        else:
            start = mid + 1
            answer = mid
    return answer 
    
  


distance = 25
rocks = [2,14,11,21,17]
n = 2
result = solution(distance, rocks, n)
print(result)