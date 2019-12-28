import re
def solution(words, queries):
    result= []
    dic = {}
    for q in queries:
        if q not in dic.keys():
            qcount=q.count('?')
            p = re.compile(q.replace("?"*qcount, "[a-z]{"+str(qcount)+"}"))
            temp = sum([1 if p.match(word) and len(word)==len(q) else 0 for word in words])
            dic[q] = temp
        result.append(dic[q])
    return result