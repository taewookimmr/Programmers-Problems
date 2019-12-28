def solution(key, lock):
    ls = len(lock)
    ks = len(key)
    lim = -(ks-1)

    def rotate(r):
        dst=[[0 for _ in range(ks)] for _ in range(ks)]
        if r == 0:
            for i in range(ks):
                for j in range(ks):
                    dst[i][j] = key[i][j]
            return dst
        if r == 1:
            for i in range(ks):
                for j in range(ks):
                    dst[ks-1-j][i] = key[i][j]
            return dst
        if r == 2 :
            for i in range(ks):
                for j in range(ks):
                    dst[ks-1-i][ks-1-j] = key[i][j] 
            return dst
        if r == 3:
            for i in range(ks):
                for j in range(ks):
                    dst[j][ks-1-i] = key[i][j] 
            return dst 

    def check():

        for row in range(lim, ls):
            for col in range(lim, ls):
                # row, col로 우상단이 정해집니다.
                for i in [0,1,2,3]:
                    rotkey = rotate(i)
                    ## 열쇠를 준비합니다.
                    slock = [[e for e in row] for row in lock]
                    ## 좌물쇠도 복사해둡니다.
                    escape = 0
         
                    for r in range(row, row+ks):
                        for c in range(col, col+ks):
                            if r >= 0 and r < ls and c >=0 and c <ls:
                                if rotkey[r-row][c-col] == slock[r][c]:
                                    escape = 1
                                    break
                                slock[r][c] += rotkey[r-row][c-col]

                        if escape :
                            break
                    if escape == 0:
                        if sum([sum([e for e in row]) for row in slock]) == ls*ls :
                            return True
        return False



    return check()

                                
                


key  = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))