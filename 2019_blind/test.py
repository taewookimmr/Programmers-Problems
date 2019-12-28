def test():
    a =[0,1,2,3,4,5,6,7,8,9]
    n = 10
    i = -3
    j = n+i
    a = a[i:] + a[:j]
    print(a)

def test1():
    a = list(map(lambda x: x*2, [e for e in range(4)]))
    print(a)


from collections import Counter
def test2():
    # a = Counter()
    li = [1,1,2,2]
    print(Counter(li))

test2()