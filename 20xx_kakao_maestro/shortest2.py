def solution(maps):
    h = len(maps)
    w = len(maps[0])
    lim = h*w+2
    for row in range(h):
        for col in range(w):
            if maps[row][col] == 1 :
                maps[row][col] = lim
    maps[h-1][w-1] = 1
    queue = [] 
    queue.append([h-1,w-1])
    while len(queue):
        r, c = queue.pop(0)
        if r == 0 and c == 0:
            break
        if r-1 >= 0 and maps[r-1][c]:
            if maps[r-1][c] > maps[r][c]:
                maps[r-1][c] = maps[r][c]+1
                queue.append([r-1,c])
        if r+1 < h and maps[r+1][c]:
            if maps[r+1][c] > maps[r][c]:
                maps[r+1][c] = maps[r][c]+1
                queue.append([r+1,c])
        if c-1 >= 0 and maps[r][c-1]:
            if maps[r][c-1] > maps[r][c]:
                maps[r][c-1] = maps[r][c]+1
                queue.append([r, c-1])
        if c+1 < w and maps[r][c+1]:
            if maps[r][c+1] > maps[r][c]:
                maps[r][c+1] = maps[r][c]+1
                queue.append([r, c+1])
    if maps[0][0] == lim:
        return -1
    return maps[0][0]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
result = solution(maps)
print(result)