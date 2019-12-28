def solution(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        bucket = []
        for cc in word:
            for c in skill :
                if c == cc :
                    bucket.append(cc)
        if len(bucket) != 0:
            chunk = "".join(bucket)
            if chunk in skill:
                if chunk[0] == skill[0]:
                    answer += 1
        else: 
            answer += 1
    return answer

def solution_other(skill, still_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill :
                if s != skill_list.pop(0):
                    break
        else :
            answer += 1
    return answer 


skill = "CBD"
skill_trees =["BACDE", "CBADF", "AECB", "BDA"]
n = solution_other(skill, skill_trees)
print(n)