def solution(board):
    # sliding window 
    h = len(board)
    w = len(board[0])
    n = min(h,w)
    
    if n==1:
        return 1
    
    rowsearch = set()
    for r in range(h):
        count = 0
        for c in range(w):
            if board[r][c] :
                count +=1
            else : 
                rowsearch.add(count)
                count = 0
        rowsearch.add(count)
        
    colsearch = set()
    for c in range(w):
        count = 0 
        for r in range(h):
            if board[r][c]:
                count +=1
            else:
                colsearch.add(count)
                count = 0
        colsearch.add(count)
    
    cross = rowsearch & colsearch 
    cross = list(cross)
    m = max(cross)
    
    search = [e for e in range(m+4,-1,-1)]
    
    for wsize in search:
        limrow = h-wsize+1
        limcol = w-wsize+1
        for row_start in range(0, limrow):
            for col_start in range(0, limcol): 
                breakcount = 0
                for i in range(row_start, row_start+wsize):
                    for j in range(col_start, col_start+wsize):
                        if board[i][j] == 0:
                            breakcount = 1
                            break
                    if breakcount == 1:
                        break
                if breakcount == 0 :
                    return wsize*wsize           