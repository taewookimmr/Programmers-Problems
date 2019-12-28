import math
        
def solution(board):

    lim = len(board)
    infinite = lim*lim+1
    board = [[infinite if e == 0 else -1 for e in row] for row in board]
    board[0][0] = 0
    board[0][1] = 0

    right,down,left,up=[0,1,2,3]
    p = [0, 0, 0, 1]    
    queue = []

    def renewal(pos, distance):
        # 움직인 후의 좌표
        r1,c1,r2,c2=pos
        
        if distance <= board[r1][c1] or distance <=board[r2][c2]:
            board[r1][c1] = min(board[r1][c1],distance)
            board[r2][c2] = min(board[r2][c2],distance)
            return  True

        return False


    def check_trans(pos):
        r1,c1,r2,c2 = pos
        #boundary condtion
        if c1 <0 or c1>=lim or c2<0 or c2>=lim or r1<0 or r1>=lim or r2<0 or r2>=lim:
            return False
        # wall condtion
        if board[r1][c1] < 0 or board[r2][c2] < 0:
            return False
        # distance condtion
        # 아니야 일단 가고, 갱신만 잘해주면 됩니다.
        return True

    # trans  할 수 있으면 True와 움직인 후의 좌표를 반환한다. 
    def move_trans(pos, distance, move): 
        # 움직이기 전의 좌표
        r1,c1,r2,c2 = pos
        if move == left:
            c1-=1
            c2-=1
        elif move == right:
            c1+=1
            c2+=1
        elif move == up:
            r1-=1
            r2-=1
        elif move ==down:
            r1+=1
            r2+=1
        if check_trans([r1,c1,r2,c2]):
            if renewal([r1,c1,r2,c2], distance+1):
                queue.append([[r1,c1,r2,c2], distance+1])


    # rotate 할 수 있으면 True와 움직인 후의 좌표를 반환한다.
    def move_rotate(pos, distance, axis=1, ccw=1):
        r1,c1,r2,c2 = pos

        delr = axis*(r2 - r1)
        delc = axis*(c2 - c1)
        normr = int(math.cos(math.pi/2*ccw)*delr - math.sin(math.pi/2*ccw)*delc)
        normc = int(math.sin(math.pi/2*ccw)*delr + math.cos(math.pi/2*ccw)*delc)

        if axis == 1: ## axis = number1
            checkr = delr+normr + r1
            checkc = delc+normc + c1
            dstr = normr +r1
            dstc = normc +c1

            ## boundary condtion
            if checkr < 0 or checkr >= lim or checkc < 0 or checkc >= lim:
                return
            
            ## boundary condtion
            if dstr < 0 or dstr>=lim or dstc < 0 or dstc >= lim:
                return

            ## wall condtion
            if board[checkr][checkc]<0 or board[dstr][dstc]<0:
                return
            else :
                if renewal([r1, c1, dstr, dstc], distance+1):
                    queue.append([[r1, c1, dstr, dstc], distance+1])
        else:
            ##
            checkr = delr+normr + r2
            checkc = delc+normc + c2
            dstr = normr + r2
            dstc = normc + c2

            if checkr < 0 or checkr >= lim or checkc < 0 or checkc >= lim:
                return
            
            if dstr < 0 or dstr>=lim or dstc < 0 or dstc >= lim:
                return

            if board[checkr][checkc]<0 or board[dstr][dstc] <0:
                return
            else :
                if renewal([dstr, dstc, r2, c2], distance+1):
                    queue.append([[dstr, dstc, r2, c2], distance+1])
        

    distance = 0
    queue.append([p, distance])

    while len(queue):

        # print(board)
        # print(len(queue))
        pos, distance = queue.pop(0)
        # print(pos)

        if board[lim-1][lim-1] < infinite:
            return board[lim-1][lim-1]
            
        for dir in [right,down, left,up]:
            move_trans(pos, distance, dir)

        for axis in [1,-1]:
            for ccw in [1,-1]:
                move_rotate(pos, distance, axis=axis, ccw=ccw)


    

    return board[lim-1][lim-1]
        


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = solution(board)
print(result)