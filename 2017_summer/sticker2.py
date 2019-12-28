
def solution(sticker):
    answer = []
    def recursive(st1, st2, depth, accum):
        depth +=1 
        st = []
        if len(st1):
            if len(st2):
                return recursive(st1, [], depth, accum) + recursive(st2, [], depth, accum)
            else :
                st = st1
        else : 
            if len(st2):
                st = st2
            else :
                return accum

        n = len(st)
        if n < 4 :
            if n == 0 :
                return accum
            else:
                return accum + max(st)
        else : 
            result = -1
            for i in range(n):
                if depth == 1:
                    if i == 0 :
                        result = recursive(st[2:-1], [], depth, accum+st[i])
                    elif i == 1 :
                        result = recursive(st[3:],  [], depth, accum+st[i])
                    elif i == n-2 : 
                        result = recursive(st[:n-3],  [], depth, accum+st[i])
                    elif i == n-1 : 
                        result = recursive(st[1:n-2],  [], depth,  accum+st[i])
                    else : 
                        line = st[i+2:] + st[:i-1]
                        result = recursive(line,  [], depth, accum+st[i])

                else : 
                    if i == 0 :
                        result = recursive(st[2:], [], depth, accum+st[i])
                    elif i == 1 :
                        result = recursive(st[3:],  [], depth, accum+st[i])
                    elif i == n-2 : 
                        result = recursive(st[:n-3],  [], depth, accum+st[i])
                    elif i == n-1 : 
                        result = recursive(st[:n-2],  [], depth,  accum+st[i])
                    else : 
                        line1 = st[i+2:]
                        line2 = st[:i-1]
                        result = recursive(line1, line2, depth, accum+st[i])
                
    
    return recursive(sticker, [], 0,  0)
    

sticker = [14, 6, 5, 11, 3, 9 , 2, 10]
result = solution(sticker)
print(result)