def solution(words, queries):
    def check(q, words):
        count = 0
        for w in words:
            if len(q)== len(w):
                for qi, wi in zip(q,w):
                    if qi != "?" and qi != wi:
                        break
                else:
                    count+=1
        return count
    
    result= []
    dic = {}
    for q in queries:
        if q not in dic.keys():
            dic[q]=check(q, words)
        result.append(dic[q])

    return result