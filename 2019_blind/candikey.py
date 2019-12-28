from itertools import combinations

def get_processed_record(relations, atom):
    n = len(relations)
    result = []
    for i in range(n):
        s = ""
        for a in atom:
            s += relations[i][a]
        result.append(s)
    return result

def is_candidate(condensed_records_list):
    check = {}
    result = True
    for m in condensed_records_list:
        if m not in check.keys():
            check[m] = 0
        else :
            result = False
            break
    return result

def update(combis, c):
    is_something_deleted = False
    c_string = ""
    for e in c:
        c_string += str(e)

    new_combis = []
    for i in range(len(combis)):
        new_combi = []
        for j in range(len(combis[i])):
            ex_string = ""
            for k in range(len(combis[i][j])):
                ex_string += str(combis[i][j][k])
            if c_string not in ex_string:
                new_combi.append(combis[i][j])
            else : 
                is_something_deleted = True
        new_combis.append(new_combi)
    return new_combis, is_something_deleted

def solution(relations):
    col = len(relations[0]) #attribute의 수 
    if col == 1 :
        return 1
    row = len(relations)
    combis = []
    for i in range(1, col+1):
        combi = list(combinations([e for e in range(col)], i))
        combis.append(combi)
    # combis[0] 은 attributes 중에서 1개 고른 경우 
    # combis[1] 은 attributes 중에서 2개 고른 경우 
    answer = 0
    is_changed = True

    control = {}
    while is_changed:
        mystring = ""
        for combi in combis:
            mystring += "".join(str(e) for e in combi)
        if mystring not in control.keys():
            control[mystring]=1
        else :
            break

        count = 0
        for i in range(len(combis)):
            for j in range(len(combis[i])):
                condensed_records_list = get_processed_record(relations, combis[i][j])
        
                if is_candidate(condensed_records_list):
                    print(combis)
                    # combis를 갱신한다.
                    combis, is_changed = update(combis, combis[i][j])
                    answer += 1
                    count = 1
                    break
    
            if count == 1:
                break
    return answer 
                
relations = [["100","ryan","music","2"],\
            ["200","apeach","math","3"],\
            ["300","tube","computer","1"],\
            ["400","con","computer","4"],\
            ["500","muzi","music","5"],\
            ["600","apeach","music","0"]]
result = solution(relations)
print(result)