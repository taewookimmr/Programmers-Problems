def solution(n, money):
    m = len(money)
    answer = []
    def recur(remain, history):
        if remain==0:
            print(id(history))
            answer.append(sorted(history[:]))
        else :
            history=history[:]
            for unit in money:
                if remain-unit>= 0:
                    history.append(unit)
                    recur(remain-unit, history[:])
    history=[]                    
    recur(n,history)
    
    answer = set(["".join(map(str, history)) for history in answer])
    print(answer)
    return len(answer)
            