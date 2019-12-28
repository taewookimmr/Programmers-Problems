def getNext(updown_list, pindex): 
    n=len(updown_list)
    none_zero_index = list(map(lambda x: min(abs(x-pindex), n-abs(x-pindex)) if updown_list[x] != 0 else n, range(n)))
    minim = min(none_zero_index)
    return none_zero_index.index(minim), minim


def solution(name):
    n = len(name)
    base = [0]*n
    temp = list(map(lambda x : ord(name[x])-ord('A'), [e for e in range(n)]))
    updown_list= list(map(lambda x : min(x, 26-x), temp))
    s = sum(updown_list)
    updown_count = s
    if s == 0:
        return 0
    
    count = 0
    # 우선 0-index 알파벳을 처리한다.
    if updown_list[0] != 0:
        updown_list[0] = 0
    
    s = sum(updown_list)
    index = 0
    while s != 0:
        index, distance = getNext(updown_list, index)
        updown_list[index] = 0
        count +=distance
        s = sum(updown_list)     
    return   updown_count + count


name  = "AABAAAAAAAB"
result = solution(name)
print(result)
## 44분 소요
