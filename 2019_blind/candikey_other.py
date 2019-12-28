def solution(relation):
    answer = []
    row = len(relation)
    col = len(relation[0])
    for i in range(1, 1 << col):
        condensed = set()
        for j in range(row): 
            tmp = ''
            for k in range(col):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            condensed.add(tmp)

        if len(condensed) == len(relation):
            is_candidate = True
            for n in answer:
                if (n & i) == n:
                    is_candidate = False
                    break
            if is_candidate:
                answer.append(i)
    return len(answer)




relations = [["100","ryan","music","2"],\
            ["200","apeach","math","3"],\
            ["300","tube","computer","1"],\
            ["400","con","computer","4"],\
            ["500","muzi","music","5"],\
            ["600","apeach","music","0"]]
result = solution(relations)
print(result)