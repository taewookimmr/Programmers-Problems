def solution(maps):
    h = len(maps)
    w = len(maps[0])
    lim = h*w
    for row in range(h):
        for col in range(w):
            if maps[row][col] == 1 :
                maps[row][col] = lim
    maps[0][0] = 1
    def go(r, c):
        #up
        if r-1 >= 0 and maps[r-1][c]:
            if maps[r-1][c] > maps[r][c]:
                maps[r-1][c] = maps[r][c]+1
                go(r-1, c)
        if r+1 < h and maps[r+1][c]:
            if maps[r+1][c] > maps[r][c]:
                maps[r+1][c] = maps[r][c]+1
                go(r+1, c)

        if c-1 >= 0 and maps[r][c-1]:
            if maps[r][c-1] > maps[r][c]:
                maps[r][c-1] = maps[r][c]+1
                go(r, c-1)
        if c+1 < w and maps[r][c+1]:
            if maps[r][c+1] > maps[r][c]:
                maps[r][c+1] = maps[r][c]+1
                go(r, c+1)
    go(0,0)
    if maps[h-1][w-1] == lim:
        return -1
    return maps[h-1][w-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
result = solution(maps)
print(result)