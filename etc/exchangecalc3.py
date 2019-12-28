def solution(n, money):
    temp = []
    for unit in money:
        if unit <= n:
            temp.append(unit)
    money = temp
    answer = 0
    queue = []
    queue.append([n, 0])
    while len(queue):
        remain, prevunit = queue.pop(0)
        for unit in money:
            if unit >= prevunit :
                if remain-unit >= unit :
                    queue.append([remain-unit, unit])
                if remain-unit == 0:
                    answer+=1
                        
    return answer%1000000007
            
