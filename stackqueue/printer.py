# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 
#    J를 대기목록의 가장 마지막에 넣습니다.

# 3. 그렇지 않으면 J를 인쇄합니다.
def getMax(zipped):
    a = [e[0] for e in zipped]
    return max(a)

def solution(pri, loc):
    count = 0
    index = [e for e in range(len(pri))]
    zipped = list(zip(pri, index))
    zipped.reverse()
    while True:
        a = zipped.pop()
        if len(zipped) > 0 and a[0] >= getMax(zipped):
            count+=1 
            if a[1] == loc :
                break
        else :
            if len(zipped) == 0:
                count+=1
                break
            zipped.insert(0, a)
    return count
    

def easy_solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans


pri = [1,1,9,1,1,1]
result = easy_solution(pri, 0)
print(result)