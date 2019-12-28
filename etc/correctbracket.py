def solution(n):
    m = n*2 ## 총길이
    answer = 0
    
    queue = []
    queue.append("1")
    while len(queue):
        history = queue.pop(0)
        a = len(history)
        x = sum(map(int,list(history)))
        y = sum([1 if e == "1" else -1 for e in history])
        
        if x==n:
            answer += 1 
            continue
        if y==0:
            queue.append(history+"1")
        else :
            queue.append(history+"1")
            queue.append(history+"0")
        
    return answer
        
            
        
        