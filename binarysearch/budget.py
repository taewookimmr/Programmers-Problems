

def solution(budgets, M):
    if M >= sum(budgets):
        return max(budgets)

    def func(limit):
        return M-sum([b if b < limit else limit for b in budgets])

    left  = M//len(budgets)
    right = max(budgets)
    while True :
        if left == right or right-left==1:
            break
        middle = (left + right)//2
        if func(middle) > 0:
            left = middle
        else : 
            right = middle
    if func(left) > 0:
        return left
    else :
        return left-1


    

    return limit-1


budgets =[120, 110, 140, 150]
M = 485
result = solution(budgets, M)
print(result)