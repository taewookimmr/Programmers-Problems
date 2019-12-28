def solution(dirs):
    prev = [5,5]
    next = [0,0]
    dic = {}
    for d in dirs:
        d2 = ""
        k2 = 0
        if d == "L":
            next = [prev[0]-1, prev[1]]
            k2 = prev[0]-1 +prev[1]*11
            d2 = "R"
        elif d == "R":
            next = [prev[0]+1, prev[1]]
            k2 = prev[0]+1 + prev[1]*11
            d2 = "L"
        elif d == "U":
            next = [prev[0], prev[1]-1]
            k2 = prev[0] + (prev[1]-1)*11
            d2 = "D"
        else :
            next = [prev[0], prev[1]+1]
            k2 = prev[0] + (prev[1]+1)*11
            d2 = "U"
        if next[0] >= 0 and next[0] <= 10 and next[1] >= 0 and next[1] <= 10:
            k1 = prev[0] + prev[1]*11
            p1 = str(k1) + d                
            p2 = str(k2) + d2

            prev = next
            if p1 not in dic.keys():
                dic[p1] = 1
                dic[p2] = 1
    print(dic)
    return len(dic)//2

dirs = "LRLRLRLR"
n = solution(dirs)
print(n)