def solution(n):
    if n==1:
        return 1
    if n <4 :
        return 0
    
    from itertools import permutations as pmt
    myperm = list(pmt(range(n)))

    answer = 0
    while len(myperm):
        perm = myperm.pop(0)
        dp =[[0 for _ in range(n)] for _ in range(n)]
        def check(r,c):
            for i in range(r,n):
                dp[i][c]=-1
            for i in range(c,n):
                dp[r][i]=-1
            i=1
            while r-i>=0 and c+i<n:
                dp[r-i][c+i]=-1
                i+=1
            i=1
            while r+i<n and c+i<n:
                dp[r+i][c+i]=-1
                i+=1
            dp[r][c] = 1 # q가 놓여 있다는 뜻의 1
        
        count = 0 
        for c in range(n):
            r = int(perm[c])
            if dp[r][c] == 0:
                check(r,c)
                count +=1
            else :
                myperm.pop()
                break
        if count == n:
            answer+=2
            myperm.pop()
        
    return answer

            
                    
