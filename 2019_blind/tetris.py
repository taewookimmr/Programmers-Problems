TETRIS = ["0231", "000211", "0013", "00-1112", "0031", "000112", "0-213", "011211", "0-113", "000121", "01131", "0-10121"]
VALID_TETRIS = [TETRIS[2], TETRIS[3], TETRIS[5],TETRIS[6], TETRIS[8]]
# 2, 3, 5, 6, 8 : possible block

def scan_line(blocks, from_ = 0):
    row = len(blocks)
    col = len(blocks[0])

    top_line = list()
    for i in range(from_, row):
        if sum(blocks[i]) > 0:
            top_line += blocks[i]
            break
    level = i

    atom = {} 
    # the key is the identific number of an block
    # the value is the list, [location(col position), count]
    for j in range(col):
        if top_line[j] != 0:
            if top_line[j] in atom.keys():
                atom[top_line[j]][1] += 1
            else :
                atom[top_line[j]] = [j, 1] # location, count        
    return atom, level



def fine_valid(blocks):
    n = len(blocks)
    layers = []
    atom, level = scan_line(blocks, from_= 0)
    layers.append([atom, level])
    for i in range(level+1, n):
        atom, level = scan_line(blocks, from_= i)
        layers.append([atom, level])

    pack = {}
    for layer in layers:
        for atom in layer[0].keys():
            if atom in pack.keys():
                pack[atom].append(layer[0][atom])
            else :
                pack[atom] = list()
                pack[atom].append(layer[1])  
                pack[atom].append(layer[0][atom])  


    for atom in pack.keys():
        s = ""
        p = ""
        for i in range(1, len(pack[atom])):
            p += str(pack[atom][i][0]-pack[atom][1][0])
            s += str(pack[atom][i][1])
        pack[atom].append(pack[atom][1][0])
        for i in range(1, len(pack[atom])-1):
            pack[atom].pop(1)
        block_type = TETRIS.index(p+s)
        pack[atom].append(block_type)
    # key >> specific number of blocks
    # value >> [row, col, block type number]
    
    return pack



def drop_that(blocks, row_col_type):
    result = 1
    row = row_col_type[0]
    col = row_col_type[1]
    type_ = row_col_type[2]

    if type_ == 2:
        row1 = row
        col1 = col+1
        col2 = col+2
        for r in range(0, row1+1):
            if blocks[r][col1] != 0 or blocks[r][col2] != 0:
                return 0
        blocks[row][col] = 0
        blocks[row+1][col] = 0
        blocks[row+1][col+1] = 0
        blocks[row+1][col+2] = 0

    elif type_ == 3:
        row1 = row+1
        col1 = col-1
        for r in range(0, row1+1):
            if blocks[r][col1] != 0:
                return 0
        blocks[row][col] = 0
        blocks[row+1][col] = 0
        blocks[row+2][col] = 0
        blocks[row+2][col-1] = 0


    elif type_ == 5:
        row1 = row+1
        col1 = col+1
        for r in range(0, row1+1):
            if blocks[r][col1] != 0:
                return 0
        blocks[row][col] = 0
        blocks[row+1][col] = 0
        blocks[row+2][col] = 0
        blocks[row+2][col+1] = 0

    elif type_ == 6:
        row1= row 
        col1 = col-2
        col2 = col-1
        for r in range(0, row1+1):
            if blocks[r][col1] != 0 or blocks[r][col2] != 0:
                return 0
        blocks[row][col] = 0
        blocks[row+1][col] = 0
        blocks[row+1][col-1] = 0
        blocks[row+1][col-2] = 0
    
    elif type_ == 8:
        row1 = row
        col1 = col-1
        col2 = col+1
        for r in range(0, row1+1):
            if blocks[r][col1] != 0 or blocks[r][col2] != 0:
                return 0
        blocks[row][col] = 0
        blocks[row+1][col] = 0
        blocks[row+1][col-1] = 0
        blocks[row+1][col+1] = 0

    return result


def solution(blocks):
    answer = 0
    bricks = fine_valid(blocks)
    for n in bricks :
        if TETRIS[bricks[n][2]] in VALID_TETRIS:
            answer += drop_that(blocks, bricks[n])
    return answer 








blocks = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
result = solution(blocks)
print(result)