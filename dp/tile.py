def solution(N):
        
    if N == 1:
        return 4

    a = [0]*(N+1)
    for i in range(1, N+1):
        if i == 1 or i == 2:
            a[i] = 1
        else :
            a[i] = a[i-1]+ a[i-2]
    
    return a[N]*4 + a[N-1]*2
    

result = solution(3)
print(result)