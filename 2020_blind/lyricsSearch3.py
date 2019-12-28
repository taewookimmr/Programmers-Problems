
def solution(words, queries):
    result= []
    dic = {}
    for q in queries:
        if q not in dic.keys():
            count = 0
            n = len(q)
            i = q.index('?')
            for word in words:
                if len(word) == n :
                    if i :
                        if word[:i] == q[:i]:
                            count +=1
                    else :
                        j = n-1-q[::-1].index('?')
                        if word[j+1:] == q[j+1:]:
                            count +=1
            dic[q]=count
        result.append(dic[q])

    return result


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)