def solution(m, n, boardoriginal):

    
    def down(boardsrc):
        for c in range(n):
            slot=[]
            for r in range(m-1, -1, -1):
                if boardsrc[r][c] != 0:
                    slot.append(boardsrc[r][c])
            zerocount = m-len(slot)
            slot+=[0]*zerocount
            for r in range(m):
                boardsrc[r][c]=slot.pop()

    def calc(boardsrc):
        return sum([sum([1 if e==0 else 0 for e in row]) for row in boardsrc ])
                    
    def find(boardsrc):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # board=[[c for c in row] for row in boardsrc]
        board=boardsrc
        findatleastoneset = False
        dir =[[1,0], [1,1], [0,1]]
        for r in range(m):
            for c in range(n):
                count = 0
                check=0
                for dr,dc in dir: 
                    if r+dr>=0 and r+dr<m and c+dc >=0 and c+dc<n:
                        if board[r][c]==board[r+dr][c+dc] and board[r][c]!=0:
                            check+=1
                        else:
                            count+=1
                            break
                if check==3:
                    dp[r][c]=1
                    findatleastoneset = True

        for r in range(m):
            for c in range(n):
                if dp[r][c]:
                    board[r][c]=0
                    for dr,dc in dir:
                        board[r+dr][c+dc] = 0
        return findatleastoneset
    
  
    board=[[e for e in row] for row in boardoriginal]

    while True:
        down(board)
        if find(board):
            pass
        else:
            break
    
    print(board)
    return calc(board)
    

                        
board=	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]           
solution(6,6,board)
            