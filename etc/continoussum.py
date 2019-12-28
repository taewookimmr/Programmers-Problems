def solution(n):
    initial = [e for e in range(1, n+1)]
    
    m = 1
    while m*(m+1) < 2*n:
        m+=1
    index = [e for e in range(1, m+1)]
    count = 0
    
    for a in initial :
        for k, b in enumerate(index):
            if a*b + b*(b-1)//2 == n:
                count +=1
                index.pop(k)
                break
    return count