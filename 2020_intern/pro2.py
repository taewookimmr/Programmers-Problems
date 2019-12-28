def solution(s):
    mystr=s[1:-1]
    queue = []
    answer =[]
    count = 0
    for c in mystr:
        if c == "}":
            answer.append(queue[:])
            queue.clear()
        else:
            if c != "{":
                queue.append(c)
    kakao = []
    for a in answer :
        temp ="".join(a)
        if temp[0] == ",":
            kakao.append(temp[1:])
        else:
            kakao.append(temp)
    frodo =[]
    for b in kakao:
        frodo.append(b.split(","))

    con = [] 
    for c in frodo :
        con.append([int(e) for e in c])
    
    con = sorted(con,key=lambda x: len(x))
    
    answer = []
    freakonaleash= set()
    for d in con:
        for e in d:
            if e not in freakonaleash:
                freakonaleash.add(e)
                answer.append(e)
                    
    return answer