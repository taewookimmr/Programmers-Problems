## 이건 수학적으로 증명해보고 싶네!

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = [0]
    for i in range(2, n+1):
        dp[i] = dp[i-1]+[0]+[0 if e else 1 for e in dp[i-1][::-1]]
    return dp[n]