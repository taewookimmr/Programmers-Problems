def solution(citations):
  
    answer = []
    for i in range(max(citations)+1):
        a = []
        for c in citations:
            if c >= i :
                a.append(i)
        if len(a) >= i :
            answer.append(i)    
    return max(answer)




def best1_solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


def best2_solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

citations = [3, 0, 6, 1, 5]
result = solution(citations)
print(result)

