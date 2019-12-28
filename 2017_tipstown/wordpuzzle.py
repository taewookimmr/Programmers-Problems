def solution(strs, t):
    strs = sorted(strs, key = lambda x : len(x), reverse = True)
    
    answer = 0
    prevlen = t[:]
    
    while(True):
        c = t[0]
        for str in strs:
            if t.count(str):
                idx = t.find(str)
                n = len(str)
                front = t[:idx]
                back = t[idx+n:]
                t=front+" "+back
                print(str)
                answer += 1
                break
                    
        if prevlen == t:
            break
        else:
            prevlen = t[:]
            
    result = list(t)
    for e in result :
        if e != " ":
            return -1
    return answer
