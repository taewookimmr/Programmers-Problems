def solution(n):
    if n==1:
        return 1
    if n <4 :
        return 0
    
    from itertools import permutations as pmt
    myperm = list(pmt(range(n)))
    m=len(myperm)

    notqueencount=0
    for k, perm in enumerate(myperm):
        if k >= m//2:
            break
        notqueen =0
        for i in range(n-1):
            for j in range(i+1,n):
                delta=j-i
                if abs(perm[i]-perm[j]) == delta:
                    notqueen=1
                    notqueencount+=1
                    break
            if notqueen:
                break
    return m-notqueencount*2

