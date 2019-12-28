def solution(n, money):
    dp=[0 for _ in range(n+1)]
    for unit in money :
        dp[unit]=1
    for i in range(1, n+1):
        for unit in money:
            if i - unit >=0:
                dp[i] += dp[i-unit]
    return dp[n]