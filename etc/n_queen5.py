import math

def permgen(n,k):

    pool = [e for e in range(n)]
    result = []
    f = math.factorial(n)

    k-=1
    while n>0:
        f //= n 
        n-=1
        result.append(pool.pop(k//f))
        k %= f

    return result


def solution(n):
    if n==1:
        return 1
    if n <4 :
        return 0

    m = math.factorial(n)
  

    notqueencount=0
    perm=permgen(n,1)
    k = 0
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
        perm=permgen(n,k)

    return m-notqueencount*2

print(solution(4))