def solution(nums):
    myset = set(nums)
    m = len(nums)//2
    if len(myset) >= m :
        return m
    else : 
        return len(myset)

nums = [3,3,3,2,2,4]
result = solution(nums)
print(result)