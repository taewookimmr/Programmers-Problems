
def solution(sticker):
    n = len(sticker)
    answer = []

    def linear_recursive(line, accum):
        m = len(line)
        if m == 0 :
            return
        if m == 1 :
            answer.append(accum +  line[0])
        elif m == 2 : 
            answer.append(accum + line[0])
            answer.append(accum + line[1])
        elif m == 3 : 
            answer.append(accum + line[1])
            linear_recursive(line[2:], accum+line[0])
            linear_recursive(line[:1], accum+line[2])
        else : 
            for j in range(m):
                if j == 0:
                    linear_recursive(line[2:], accum+line[j])
                elif j == 1 : 
                    linear_recursive(line[3:], accum+line[j])
                elif j == m-2:
                    linear_recursive(line[:m-3], accum+line[j])
                elif j == m-1:
                    linear_recursive(line[:m-2], accum+line[j])
                else :
                    linear_recursive(line[:j], accum+line[j])
                    linear_recursive(line[j+1:], accum+line[j])
        
    def init(initiator):
        line = []
        
        if initiator == 0:
            line = sticker[2:-1]
        elif initiator == 1:
            line = sticker[3:]
        elif initiator == n-2:
            line = sticker[:-3]
        elif initiator == n-1:
            line = sticker[1:-2]
        else : 
            line = sticker[initiator+2:] + sticker[:initiator-1]
 
        linear_recursive(line, sticker[initiator])

    if n < 4 :
        return max(sticker)
    else : 
        for i in range(n):
            init(i)

    return max(answer)

    

sticker = [14, 6, 5, 11, 3, 9 , 2, 10]
result = solution(sticker)
print(result)