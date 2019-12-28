
def solution(strs, t):
    
    answer = []
    queue = []
    for str in strs:
        if t.count(str) != 0 and t.find(str) == 0:
            queue.append([1, str])
    
    while len(queue):
        level, accum = queue.pop(0)
        if accum == t:
            answer.append(level)
            break
        else :
            for str in strs:
                n = len(accum)
                remain = t[n:]
                if remain.count(str) != 0 and remain.find(str) == 0:
                    queue.append([level+1, accum+str])
    if len(answer):
        return min(answer)
    else:
        return -1
    
        