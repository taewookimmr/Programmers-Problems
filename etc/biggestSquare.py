def solution(board):
    # sliding window 
    h = len(board)
    w = len(board[0])
    n = min(h,w)
    
    if n==1:
        return 1
        
    for wsize in range(n, -1, -1):
        limrow = h-wsize+1
        limcol = w-wsize+1
        for row_start in range(0, limrow):
            for col_start in range(0, limcol): 
                expectation = wsize*wsize
                
                for i in range(row_start, row_start+wsize):
                    if sum(board[i][col_start:col_start+wsize]) == wsize :
                        expectation-=wsize
                    else:
                        break
                if expectation==0:
                    return wsize*wsize
                        
            
            