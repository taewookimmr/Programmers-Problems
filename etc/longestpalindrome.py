# 그냥 sliding window가 답이었네 
def solution(s):
    n=len(s)
    for expectation in range(n,0,-1):
        for i in range(0,  n-expectation+1):
            test=s[i:i+expectation]
            if test==test[::-1]:
                return expectation
    return 1
        

## 쓸데없이 dp로 접근, 더군다나 논리적 오류도 포함된 것으로 판단됨
def solution(s):
    import sys
    sys.setrecursionlimit(10*6)
    n = len(s)
    dp=[0 for _ in range(n)]
    dpe=[0 for _ in range(n)]
    def scanning_odd(x,d):
        if x-d>=0 and x+d<n:
            if s[x-d] == s[x+d]:
                dp[x-d] = max(dp[x-d], d)
                dp[x+d] = max(dp[x+d], d)
                scanning_odd(x,d+1)
    def scanning_even(x,d):
        if x+1<n and s[x]==s[x+1]:
            if x-d>=0 and x+1+d<n:
                if s[x-d] == s[x+1+d]:
                    dpe[x-d]=max(dpe[x-d],d)
                    dpe[x+1+d]=max(dpe[x+1+d],d)
                    scanning_even(x,d+1)
                
    for i in range(n):
        scanning_odd(i,1)
        scanning_even(i,0)
    
    a = max(dp)*2+1
    b = max(dpe)*2
    return max(a,b)