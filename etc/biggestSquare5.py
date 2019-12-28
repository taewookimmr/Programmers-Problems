def solution(board): ## finally 
    
    h = len(board)
    w = len(board[0])
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            dp[i][j] = board[i][j]

    adj = [[1,0], [1,1], [0,1]]    
    for i in range(h):
        for j in range(w):
            if dp[i][j] and dp[i+1][j+1]:
                dp[i+1][j+1] = max(dp[i+1][j+1], min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1)     
    x = max( [max(row) for row in dp])
    return x*x
 
     
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))