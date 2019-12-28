def solution(board): ## 이분 탐색.. 이 느낌 아닙니다.
    # sliding window 
    h = len(board)
    w = len(board[0])
    n = min(h,w)
    
    if n==1:
        return 1

    right = n
    left = 0 

    answer = set()
    while left <= right : 
        wsize =(left+right)//2
        limrow = h-wsize+1
        limcol = w-wsize+1
        
        possible = False
        for row_start in range(0, limrow):
            for col_start in range(0, limcol): 
                upperrightcheck = 0
                for i in range(row_start, row_start+wsize):
                    for j in range(col_start, col_start+wsize):
                        if board[i][j] == 0:
                            upperrightcheck = 1
                            break
                    if upperrightcheck == 1:
                        break
                if upperrightcheck == 0 :
                    possible=True
                    answer.add(wsize)
                    left = wsize+1
        if possible == False:
            right = wsize -1          

    x = max(answer)
    return x*x

                
                          