##신기한데?
def binomial(bin, n, k):
    if n==k or k==0 : return 1
    elif bin[n][k] > 0 : return bin[n][k]
    else :
        bin[n][k] = binomial(bin, n-1, k) + binomial(bin, n-1, k-1)
        return bin[n][k]

def solution(n):
    bin = [[0 for col in range(2*n + 1)] for row in range(2*n + 1)]
    return binomial(bin, 2*n, n) - binomial(bin, 2*n, n+1)

## 점화식
def solution(n):
    from math import factorial as f
    return f(2*n)//(f(n+1)*f(n))