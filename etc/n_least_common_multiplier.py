def solution(arr):
    def gcd(a,b):
        if a<b:
            t=a
            a=b
            b=t
        if b==0:
            return a
        else:
            return gcd(a%b,b)
            
    def lcm(a,b):
        x=gcd(a,b)
        aa = a//x
        bb = b//x
        return aa*bb*x
    
    while len(arr):
        a = arr.pop()
        if len(arr):
            b = arr.pop()
            arr.append(lcm(a,b))
        else :
            return a
        