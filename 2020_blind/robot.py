import math
class pos:
    def __init__(self, r, c):
        self.r=r
        self.c=c
        
class robot:
    def __init__(self, map):
        self.p1 = pos(0, 0)
        self.p2 = pos(0, 1)
        self.map = map[:]
        self.size = len(map)
        self.dp = [[self.size*self.size for e in row] for row in map]
        self.dp[0][0] =0
        self.dp[0][1] =0
        self.accumulate = 0
        ## dp[row][col] 해당 위치까지 가기 위해 필요한 최소 조작 횟수를 저장, 갈 수 없는 곳은 -1
        
    def check(self):

        lim = self.size
        r = self.p1.r
        c = self.p1.c
        ## p1이 map 밖에 있어요
        if r < 0 or r >= lim or c < 0 or c >=lim:
            return False
        
        ## p1이 벽에 있어요
        if self.map[r][c] ==1 :
            return False
        
        r = self.p2.r
        c = self.p2.c
        ## p2이 map 밖에 있어요
        if r < 0 or r >= lim or c < 0 or c >=lim:
            return False
        
        ## p2이 벽에 있어요
        if self.map[r][c] ==1 :
            return False
        
        return True
        
    def condition(self, count, operation):

        determine = 0
        if count <= self.dp[self.p1.r][self.p1.c]:
            determine+=1
        if count <= self.dp[self.p2.r][self.p2.c]:
            determine+=1
        if determine > 0:
            self.dp[self.p1.r][self.p1.c] = min(count, self.dp[self.p1.r][self.p1.c])
            self.dp[self.p2.r][self.p2.c] = min(count, self.dp[self.p2.r][self.p2.c])
            # self.dp[self.p1.r][self.p1.c] = count
            # self.dp[self.p2.r][self.p2.c] = count
            return True
        else:
            return False
    
    def left(self):
        self.p1.c -=1
        self.p2.c -=1
        if self.check():
            return True
        else :
            self.right()
            return False

    def right(self):
        self.p1.c +=1
        self.p2.c +=1
        if self.check():
            return True
        else:
            self.left()
            return False
    
    def up(self):
        self.p1.r -=1
        self.p2.r -=1
        if self.check():
            return True
        else:
            self.down()
            return False
   
    def down(self):
        self.p1.r +=1
        self.p2.r +=1
        if self.check():
            return True
        else :
            self.up()
            return False

    def rot(self, p1 = 1, ccw=1): ## p1 (1 or -1), ccw (1 or -1)
        delr = p1*self.p2.r - p1*self.p1.r
        delc = p1*self.p2.c - p1*self.p1.c
        normr = int(math.cos(math.pi/2*ccw)*delr - math.sin(math.pi/2*ccw)*delc)
        normc = int(math.sin(math.pi/2*ccw)*delr + math.cos(math.pi/2*ccw)*delc)
        if p1 == 1: ## axis = p1
            ##
            checkr = delr+normr + self.p1.r
            checkc = delc+normc + self.p1.c
            dstr = normr +self.p1.r
            dstc = normc +self.p1.c

            if checkr < 0 or checkr >= self.size or checkc < 0 or checkc >= self.size:
                return False
            
            if dstr < 0 or dstr>=self.size or dstc < 0 or dstc >= self.size:
                return False

            if self.map[checkr][checkc]==1 or self.map[dstr][dstc]==1:
                return False
            else :
                self.p2.r = dstr
                self.p2.c = dstc
                return True
        else:
            ##
            checkr = delr+normr + self.p2.r
            checkc = delc+normc + self.p2.c
            dstr = normr +self.p2.r
            dstc = normc +self.p2.c

            if checkr < 0 or checkr >= self.size or checkc < 0 or checkc >= self.size:
                return False
            
            if dstr < 0 or dstr>=self.size or dstc < 0 or dstc >= self.size:
                return False

            if self.map[checkr][checkc] or self.map[dstr][dstc]:
                return False
            else :
                self.p1.r = dstr
                self.p1.c = dstc
                return True

    def reset(self, p1, p2):
        self.p1.r = p1.r
        self.p1.c = p1.c
        self.p2.r = p2.r
        self.p2.c = p2.c

    def action(self, count, history):
        print(history[:],"\n")
        memo_p1 = pos(self.p1.r, self.p1.c)
        memo_p2 = pos(self.p2.r, self.p2.c)      

        self.reset(memo_p1, memo_p2)   
        if self.left():
            if self.condition(count+1,"left"):
                self.action(count+1, history +"left ")
            else: 
                self.right()

        self.reset(memo_p1, memo_p2)        
        if self.right():
            if self.condition(count+1, "right"):
                self.action(count+1, history+"right ")
            else: 
                self.left()

        self.reset(memo_p1, memo_p2)            
        if self.up():
            if self.condition(count+1,"up"):
                self.action(count+1, history+"up ")
            else: 
                self.down()

        self.reset(memo_p1, memo_p2)            
        if self.down():
            if self.condition(count+1, "down"):
                self.action(count+1, history+"down ")
            else: 
                self.up()

        for axis in [1,-1]:
            for ccw in [1,-1]:
                self.reset(memo_p1, memo_p2)    
                if self.rot(p1=axis, ccw=ccw):
                    if self.condition(count+1, "rotate"+str(axis)+str(ccw)):
                        self.action(count+1, history+"rotate"+str(axis)+str(ccw)+" ")
                    else: 
                        self.rot(p1=axis, ccw=ccw*(-1))
        
def solution(board):
    quanx = robot(board)
    quanx.action(0, "origin ")  
    n = len(board)
    print(quanx.dp)
    return quanx.dp[n-1][n-1]


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = solution(board)
print(result)