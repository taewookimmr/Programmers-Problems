def solution(n):
    m = n*2 ## 총길이
    answer = 0
    
    queue = []
    queue.append([1, 0])
    while len(queue):
        one, zero = queue.pop(0)
        if one==n:
            answer += 1 
            continue
        if one==zero:
            if one+1==n:
                answer+=1
            else :
                queue.append([one+1, zero])
        else :
            if one+1==n:
                answer+=1
            else :
                queue.append([one+1, zero])
                
            queue.append([one, zero+1])
        
    return answer
        
            
        
        