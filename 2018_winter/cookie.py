def solution(cookie):
    answer = 0
    accum = [0 for _ in range(2001)]
    n = len(cookie)
    for i in range(n):
        sum[i+1] = sum[i] + cookie[i]
    for m in range(1, n):
        c = accum[m]
        for r in range(m+1, n+1):
            s = accum[r] - c
            if answer >= s or s > c :
                continue
            for l in range(m):
                if s == c-accum[l]:
                    answer = max(answer, s)
                    break
    return answer 

def solution_others(cookie):
    from itertools import accumulate
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b
        if c :
            print("what the fuck", type(c))
            answer = max(*c, answer )
    return answer 

cookie = [1,1,2,3]
n = solution_others(cookie)

print(n)