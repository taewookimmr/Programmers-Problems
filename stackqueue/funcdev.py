def solution(p, s):
    
    answer = []
    while p:   
        count = 0
        for i in range(len(p)):
            p[i] = p[i] + s[i]
        while p :
            if p[0] >= 100:
                p.pop(0)
                s.pop(0)
                count+=1
            else :
                break
        if count != 0:
            answer.append(count)
        
    return answer 


# 190903 아직 이해 못함.
def best_solution(pro, spe):
    q = []
    for p, s in zip(pro, spe):
        print(q)
        if len(q) == 0 or q[-1][0] < (100-p)//s:
            q.append([(100-p)//s, 1])
        else : 
            q[-1][1] += 1
    return [qq[1] for qq in q]

pro = [93, 30, 55]
spe = [1, 30, 5]
result = best_solution(pro,spe)
print(result)