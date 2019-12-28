
def solution(f, k):
    d = {}
    for idx, t in enumerate(f):
        if t in d:
            d[t].append(idx)
        else:
            d[t] = [idx]

    n = len(f) # the number of food
    c = 0
    for t in sorted(d):
        if k >= n*(t-c) :
            k -= n*(t-c)
            n -= len(d[t])
            c = t
        else:
            k %= n
            for i in d:
                if i >= t:
                    idx = d[i][0]
                    break
            for i in range(idx, len(f)):
                if f[i] >= t:
                    k -= 1
                    if k < 0:
                        return i+1
                    
    return -1
    
    
food_times  = [4,1,1,1,3,10]
k = 9
result = solution(food_times, k)
print(result)
