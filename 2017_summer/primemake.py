def isPrime(num):
    if num == 1 :
        return False
    if num == 2 :
        return True

    import math
    lim = int(math.sqrt(num))
    for i in range(2, lim+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n = len(nums)
    from itertools import combinations
    combi=list(combinations(nums,3))
    m = len(combi)
    for tup in combi:
        if isPrime(sum(tup)):
            answer += 1
    return answer 
        

nums = [1,2,3,4]
n = solution(nums)
print(n)