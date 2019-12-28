# 되도록이면 짧은 심사를 하는 심사관에게 심사받는 것이 좋다. 
# 목표 함수를 어떻게 설정해야할까?



def solution(n, times):
    times.sort()
    m = len(times)
    maxim = max(times)
    left = 1 
    right = maxim*n 
    result = maxim*n 
    while(left<=right):
        mid = (left+right)//2
        total = 0
        for i in range(m):
            total += mid // times[i]
        
        if total < n :
            left = mid + 1
        else :
            if result > mid:
                result = mid
            right = mid -1
    return result

n = 6
times = [7, 10]
result = solution(n, times)
print(result)