
def slow_solution(weight):
    weight.sort()
    n = len(weight)

    target = 1
    while True:
        for i in range(1, 1<<n):
            tar = target 
            whilescape = False
            for j in range(n):
                if i & (1 << j):
                    tar -= weight[j]
                    if tar < 0:
                        break
                    if tar == 0:
                        whilescape = True
                        break
            if whilescape == True:
                break
        if whilescape == True:
            target += 1
        else : 
            break

    return target

def modi_solution(weight):
    weight.sort()
    n = len(weight)

    target = 1
    while True:
        tar = target
        for i in range(1, 1<<n):
            combi = [weight[j] for j in range(n) if i & (1<<j)]
            if sum(combi) == tar :
                target+=1
                break
        if tar == target:
            break

    return target
    
def solution(weight):
    weight.sort()
    ans = 1
    for e in weight:
        if e > ans:
            break
        ans += e


    return ans


weight = [1,2,4,7,15,29,50]
result = solution(weight)
print(result)