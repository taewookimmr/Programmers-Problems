def solution(participant, completion):  
    dic = {}
    for p in participant :
        if p in dic.keys():
            dic[p] += 1
        else :
            dic[p] = 1
    for c in completion:
        dic[c] -= 1
    
    for p in participant:
        if dic[p] > 0 :
            return p

def soltion_other(part, comp):
    import collections
    answer = collections.Counter(part) - collections.Counter(comp)
    print(answer)
    return list(answer.keys())[0]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
completion = ["josipa", "filipa", "marina", "nikola"]

print(soltion_other(participant, completion))