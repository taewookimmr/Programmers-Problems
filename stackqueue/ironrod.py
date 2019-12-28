def incomplete_solution(arr):
    l = " ".join(arr)
    l = list(l.split())
    l = [0 if e == '(' else 1 for e in l]
    laser = []
    left = []
    for i in range(len(l)-1):
        if l[i] == 0 and l[i+1] == 1:
            laser.append(i)
        elif l[i] == 0:
            left.append(i)

    laser_total = laser + [e+1 for e in laser]
    right = list(set([e for e in range(len(l))]) - set(laser_total) - set(left))
    zipped = list(zip(left, right))
    
    initial_rod = len(zipped)
    answer = initial_rod
    for i in range(initial_rod):
        for j in laser :
            if zipped[i][0] < j and j < zipped[i][1]:
                answer += 1
    return answer 

def solution(arr):
    l = " ".join(arr)
    l = list(l.split())
    l = [0 if e == '(' else 1 for e in l]
    answer = 0
    stack = [] 
    i = 0
    while i < len(l):
        if l[i] == 0 and i+1 < len(l) and l[i+1] ==1 :
            # laser 
            i += 1
            answer += len(stack)
        elif l[i] == 0 and i+1 < len(l) and l[i+1] ==0 :
            # rod 시작
            stack.append(0)
        elif l[i] == 1 :
            # rod 끝 
            stack.pop()
            answer += 1
        i +=1
    return answer

def best_solution(arr):
    answer = 0
    stack = 0
    laseron =False
    for p in arr :
        if p == '(':
            laseron = True
            stack += 1
        else : 
            if laseron == True:
                answer += stack-1
                laseron = False
            else :
                answer += 1
            stack -= 1
    return answer

def great_solution(arr):
    answer = 0
    sticks = 0
    modi = arr.replace('()', '0')
    for i in modi :
        if i == '(':
            sticks += 1
        elif i == '0':
            answer += sticks
        else :
            sticks -=1
            answer +=1
    return answer 

arr = "()(((()())(())()))(())"
answer = great_solution(arr)
print(answer )