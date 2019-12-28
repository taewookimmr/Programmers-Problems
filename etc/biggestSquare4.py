def solution(board): ## 잘못된 접근입니다.
    
    # sliding window 
    h = len(board)
    w = len(board[0])
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            dp[i][j] = board[i][j]

    search = [[1,0],[1,1],[0,1]]
    queue = []
    queue.append([0,0])
    while len(queue):
        r,c = queue.pop(0)
        if r>=0 and r<h and c>=0 and c<w:
            for dr,dc in search:
                pr=r+dr
                pc=c+dc
                if pr>=0 and pr<h and pc>=0 and pc<w:
                    queue.append([r+dr, c+dc])
            if dp[r][c] and dp[r+1][c] and dp[r+1][c+1] and dp[r][c+1]:
                dp[r+1][c+1] = max(dp[r][c]+1, dp[r+1][c+1])
    x = max([max([e for e in row]) for row in dp])
    return x*x        
     
 
     
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))