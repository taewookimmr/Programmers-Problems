def solution(n, lost, reserve):
    r_set = set(reserve)
    l_set = set(lost)
    real_r = r_set - l_set 
    real_l = l_set - r_set
    helper= {}
    for e in real_r:
        helper[e] = list()
        if e-1 in real_l:
            helper[e].append(e-1)
        if e+1 in real_l:
            helper[e].append(e+1)

    h = sorted(helper.items())
    h = sorted(h, key = lambda x: len(x[1]))
    print(h)
    for e in h :
        if len(e[1]) == 1:
            if e[1][0] in real_l:
                real_l.remove(e[1][0])
        elif len(e[1]) == 2:
            if e[1][0] in real_l:
                real_l.remove(e[1][0])
            else :
                if e[1][1] in real_l:
                    real_l.remove(e[1][1])
    
    return n - len(real_l)


def best_solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost    = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r-1
        b = r+1
        if f in _lost :
            _lost.remove(f)
        elif b in _lost :
            _lost.remove(b)
    return n - len(_lost)

n =5 
lost = [2,4]
reserve = [1,3,5]

result = solution(n, lost, reserve)
print(result)



