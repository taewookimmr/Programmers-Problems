def solution(n, money):
    m = len(money)
    answer = 0
    queue = []

    queue.append([0, 0, " "])
    while len(queue):
        accum, prevunit, history = queue.pop(0)
        if accum == n :
            print(accum, prevunit , "history : ",history)
            answer+=1
        if accum < n:
            for unit in money:
                if unit >= prevunit and accum+unit <= n:
                    queue.append([accum+unit, unit, history+" "+str(unit)])
    return answer
            

## 무슨차이지!!!

def solution_incorrect(n, money):
    m = len(money)
    answer = 0
    queue = []
    for unit in money:
        if unit <= n:
            queue.append([0, unit, str(unit)])
    while len(queue):
        accum, prevunit, history = queue.pop(0)
        if accum == n :
            print(accum, prevunit , "history : ",history)
            answer+=1
        if accum < n:
            for unit in money:
                if unit >= prevunit and accum+unit <= n:
                    queue.append([accum+unit, unit, history+" "+str(unit)])
    return answer






            
n = 5
money =[1,2,5]
solution(n,money)