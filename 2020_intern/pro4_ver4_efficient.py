
def solution_recur(k, room_number):
    check = [0 for _ in range(k+1+1)]
    result= []

    def renewal(want):

        def right_check(want):
            if check[want+1]:
                check[want]= check[want+1]+1
            else:
                check[want]=1
        def left_propagate(want):
            if want-1 >= 1 and check[want-1]:
                check[want-1]=check[want]+1
                left_propagate(want-1)

        if check[want] == 0:
            result.append(want)
            right_check(want)
            left_propagate(want)
        else :
            allocated = want+check[want]
            renewal(allocated)

    for want in room_number:
        renewal(want)
    return result

def solution_ver1(k, room_number):
    check = [0 for _ in range(k+1)]
    p = len(room_number)
    result= [0 for _ in range(p)]
    
    for i,want in enumerate(room_number):
        if check[want] == 0:
            result[i] = want
            check[want]=1
        else : 
            testcheck = check[want:]
            emptyindex=0
            if testcheck.count(0) !=0:
                emptyindex = testcheck.index(0)
            alterroom = want + emptyindex
            
            result[i]=alterroom
            check[alterroom]=1
    return result

## 기본적인 탐색
def solution_ver2(k, room_number):
    check = [0 for _ in range(k+1)]
    result= []
    for want in room_number:
        if check[want] == 0:
            result.append(want)
            check[want]=1
        else : 
            for j in range(want,k+1):
                if check[j]==0:
                    result.append(j)
                    check[j]=1
                    break
    return result

## set 함수 이용
def solution_ver3(k, room):
    ## why is k needed? 
    room_number=room[:]
    v=len(room_number)
    for i in range(v):
        if i :
            left = set(room_number[:i])
            maxim = max(left)
            rni = room_number[i]
            if  rni == maxim:
                room_number[i]+=1
            elif rni < maxim:
                while True:
                    if rni in left:
                        rni+=1
                    else:
                        break
                room_number[i]=rni
    return room_number

## recursive expression
def solution_ver4(k, room_number):
    remain = [e for e in range(1,k+1)]
    def right(x):
        if remain.count(x):
            return remain.pop(remain.index(x))
        else : 
            return right(x+1)
    # remain[0]에는 남아 있는 방 중에 가장 작은 번호의 방이 있다
    return [remain.pop(0) if want <= remain[0] else right(want) for want in room_number]

## binary search
def solution_ver5(k,room_number):
    c=[e for e in range(1,k+1)]
    def binarysearch(x):
        if c.count(x):
            l = 0
            r = len(c)-1
            while True:
                m = (l+r)//2
                if c[m] > x :
                    r=m-1
                else :
                    l=m+1
                    if c[m]==x:
                        return c.pop(m)
        else:
            return binarysearch(x+1)
    return [c.pop(0) if w<=c[0] else binarysearch(w) for w in room_number]

## union-find version1
def solution_ver6(k, room_number):
    FIND=0
    UNION=1
    height = [0 for _ in range(k+1)]
    parent = [-1 for _ in range(k+1)] # 빈방은 자기가 부모다.

    def union_set(e1,e2):
        parent[e1]=e2
    def union_set2(e1,e2):
        if height[e1] == height[e2]:
            height[e2]+=1
        if height[e1] >height[e2]:
            t=e1
            e1=e2
            e2=t
        parent[e1]=e2
    def find_set(e1, e2, flag):
        i=e1
        j=e2
        while parent[i]>=0:
            i=parent[i]
        while parent[j]>=0:
            j=parent[j]
        if i!=j and flag == UNION:
            union_set(i,j)         
        if i==j:
            return True
        else :
            return False
    def find_set2(e1, e2, flag):
        i=e1
        j=e2
        while parent[i]>=0:
            i=parent[i]
        while parent[j]>=0:
            j=parent[j]
        if i!=j and flag == UNION:
            union_set2(i,j)         
        if i==j:
            return True
        else :
            return False

    answer =[]
    for want in room_number:
        if parent[want]==-1: #빈방을 요청한 경우 
            answer.append(want)
            parent[want]=-2 ## 양 옆이 비어있고 자기만 채워진 경우 -2로 유지가 된다.
            if want-1 and answer.count(want-1):
                find_set(want, want-1, UNION)
            if want+1<=k and answer.count(want+1):
                find_set(want, want+1, UNION)
        else : #이미 채워진 방을 요청한 경우
            #해당 집합에서 가장 큰 녀석의 오른쪽 자리를 할당해 준다.
            candis=[]
            for candi in range(want, k+1):
                if find_set(want, candi, FIND):
                    candis.append(candi)
            newhome = max(candis)+1
            parent[newhome]=parent[want]
            answer.append(newhome)
            if newhome+1<=k and answer.count(newhome+1):
                find_set(newhome, newhome+1, UNION)
    return answer

## union-find version2
def solution_ver7(k, room_number):
    FIND=0
    UNION=1
    height = [0 for _ in range(k+1)]
    parent = [-1 for _ in range(k+1)] # 빈방은 자기가 부모다.

    def union_set(e1,e2):
        parent[e1]=e2
    def union_set2(e1,e2):
        if height[e1] == height[e2]:
            height[e2]+=1
        if height[e1] >height[e2]:
            t=e1
            e1=e2
            e2=t
        parent[e1]=e2
    def find_set(e1, e2, flag):
        i=e1
        j=e2
        while parent[i]>=0:
            i=parent[i]
        while parent[j]>=0:
            j=parent[j]
        if i!=j and flag == UNION:
            union_set(i,j)         
        if i==j:
            return True
        else :
            return False
    def find_set2(e1, e2, flag):
        i=e1
        j=e2
        while parent[i]>=0:
            i=parent[i]
        while parent[j]>=0:
            j=parent[j]
        if i!=j and flag == UNION:
            union_set2(i,j)         
        if i==j:
            return True
        else :
            return False

    answer =[]
    for want in room_number:

        if parent[want]==-1: #빈방을 요청한 경우 
            answer.append(want)
            parent[want]=-2 ## 양 옆이 비어있고 자기만 채워진 경우 -2로 유지가 된다.
            if want-1 and answer.count(want-1):
                find_set2(want, want-1, UNION)
            if want+1<=k and answer.count(want+1):
                find_set2(want, want+1, UNION)
        else : #이미 채워진 방을 요청한 경우
            #해당 집합에서 가장 큰 녀석의 오른쪽 자리를 할당해 준다.
            candis=[]
            for candi in range(want, k+1):
                if find_set2(want, candi, FIND):
                    candis.append(candi)
            newhome = max(candis)+1
            parent[newhome]=parent[want]
            answer.append(newhome)
            if newhome+1<=k and answer.count(newhome+1):
                find_set2(newhome, newhome+1, UNION)            
    return answer

## solution_ver2를 수정한 것임
def solution_ver8(k, room_number):
    check = [0 for _ in range(k+1)]
    def unoccupied(want):
        check[want]=1
        return want 
    def preoccupied(want):
        for j in range(want,k+1): # 순차 탐색의 한계
            if check[j]==0:
                check[j]=1
                return j
    return [preoccupied(want) if check[want] else unoccupied(want) for want in room_number]

## ver8과 union-find 결합    
def solution_ver9(k, room_number):
    FIND=0
    UNION=1

    height = [0 for _ in range(k+1)]
    parent = [-1 for _ in range(k+1)] # 빈방은 자기가 부모다.

    def union_set2(e1,e2):
        if height[e1] == height[e2]:
            height[e2]+=1
        if height[e1] >height[e2]:
            t=e1
            e1=e2
            e2=t
        parent[e1]=e2
    def find_set2(e1, e2, flag):
        i=e1
        j=e2
        while parent[i]>=0:
            i=parent[i]
        while parent[j]>=0:
            j=parent[j]
        if i!=j and flag == UNION:
            union_set2(i,j)         
        if i==j:
            return True
        else :
            return False

    check = [0 for _ in range(k+1)]

    def neighbor(want, dir): 
            if want+dir and check[want+dir]:
                parent[want+dir]=want
                neighbor(want+dir, dir)

    def unoccupied(want):
        parent[want]=-2
        check[want]=1
        neighbor(want, -1)
        neighbor(want, +1)
        return want 

    def preoccupied(want):
        save =parent[want]
        want += parent[want:].index(-1)
        parent[want]=save
        check[want]=1
        neighbor(want, +1)
        return want
    return [preoccupied(want) if check[want] else unoccupied(want) for want in room_number]

def solution_ver10(k, room_number):
    check = [0 for _ in range(k+1)]
    answer=[]

    def update():
        for i in range(k, 0, -1):
            if check[i] and i-1>=1 and check[i-1] :
                check[i-1]=check[i]

    def allocate(z):
        if z+1<=k and check[z+1]:
            check[z]=check[z+1]
        else:
            check[z]=z+1
        answer.append(z)

    for want in room_number:
        if check[want]==0:
            allocate(want)
        else:
            go=check[want]
            allocate(go)
        update()

    return answer

import time
def test(function, repeat=100000):
    
    k = 15
    room_number = [1,3,4,1,5,2,8,8,10,13,1,2,3]
    start = time.time()
    for i in range(repeat):
        # print(function(k,room_number))
        function(k,room_number)
    print(time.time()-start, " second")

test(solution_ver1)
test(solution_ver2)
# test(solution_ver3)
# test(solution_ver4)
# test(solution_ver5)
# test(solution_ver6)
# test(solution_ver7)
# test(solution_ver8)
# test(solution_ver9)
test(solution_ver10)
# test(solution_recur)