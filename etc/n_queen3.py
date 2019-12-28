def permgen(n, preperm):
    if len(preperm) == 0:
        return [e for e in range(n)]
    for i in range(n-1, 0, -1):
        if preperm[i-1] < preperm[i]:
            left = preperm[:i-1]
            standard = preperm[i-1]
            right=preperm[i:]
            pivot = min( [e if e>standard else n for e in right] )
            right.remove(pivot)
            right.append(standard)

            return left + [pivot] +sorted(right)
    return []

import math
def solution(n):
    if n==1:
        return 1
    if n <4 :
        return 0

    m = math.factorial(n)
    k = 0
    perm=permgen(n,[])
    notqueencount=0

    while True:
        if k >= m//2:
            break
        k+=1
        escape =0
        for i in range(n-1):
            for j in range(i+1,n):
                delta=j-i
                if abs(perm[i]-perm[j]) == delta:
                    escape=1
                    notqueencount+=1
                    break
            if escape:
                break
        perm=permgen(n,perm)

    return m-notqueencount*2

print(solution(4))