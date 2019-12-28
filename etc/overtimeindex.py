def solution(n, works):
    if sum(works) <=n :
        return 0
        
    m = len(works) 
    queue = [[]]
    answer =[]

    while len(queue):
        if len(queue[0]) == m:
            plan = queue.pop(0)
            if sum(plan) == n:
                x=sum( [ (a-b)**2 for a,b in zip(works, plan)])
                answer.append(x)        
        else : 
            plan_precursor = queue.pop(0)
            pidx = len(plan_precursor)
            left = n-sum(plan_precursor) 
            if pidx==m-1:
                if left <= works[pidx]:
                    queue.append(plan_precursor[:]+[left])
            else:
                for i in range(0, works[pidx]+1):
                    if i <=left:
                        queue.append(plan_precursor[:]+[i])
        
    return min(answer)

works = [5,4,3,2]
n = 10
result = solution(n, works)
print(result)