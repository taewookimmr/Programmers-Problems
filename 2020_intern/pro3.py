def solution(user_id, banned_id):
    import itertools
    bn = len(banned_id)
    perm = list(itertools.permutations(user_id, bn))

    dic = {}
    for i, user in enumerate(user_id):
        dic[user]=i
        
    answer = []
    for oneperm in perm:
        count=0
        n = len(oneperm)
        for ban, user in zip(banned_id, oneperm):
                if len(ban) == len(user):
                    indicator = sum([0 if e==a or e=="*" else 1 for e,a in zip(ban, user)])
                    if indicator == 0: ## 해당 조건을 만족한다.
                        count+=1
                    else:
                        break
                else :
                    break
        if count == n:
            answer.append(oneperm)
            
    temp=[]
    temp=set(temp)
    for kakaotexi in answer:
        kakaotexi=list(kakaotexi)
        kakaotexi=sorted(kakaotexi)
        kakaotexi="".join(kakaotexi)
        temp.add(kakaotexi)
    return len(temp)