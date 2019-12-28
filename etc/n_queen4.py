# 다른 사람 코드 해석 
def solution(n):
    if n == 1:
        return 1
    if n < 4:
        return 0
    
    count = [0]
    dp = [0 for _ in range(n+1)]

    def test(x):
        for i in range(x):
            if dp[i] == dp[x]: #같은 열인지 판단
                return False
            if abs(dp[i]-dp[x]) == x-i:
                return False
        return True

    def recursive(x,prev):
        if x==n:
            count[0]+=1
        else:
            for i in range(n):
                if i != prev:
                    dp[x]=i
                    if test(x):
                        recursive(x+1,i)
                        
    recursive(0,-1)
    
    return count[0]