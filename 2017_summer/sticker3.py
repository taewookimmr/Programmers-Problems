def solution(sticker):
    n = len(sticker)
    if n < 4:
        return max(sticker)
    
    dp = [-1 for _ in range(n)]
    # first sticker peel off
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, n-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    answer = dp[n-2]

    # first sticker not peel off
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    answer = max(answer, dp[n-1])
    return answer

    


sticker = [14, 6, 5, 11, 3, 9 , 2, 10]
result = solution(sticker)
print(result)