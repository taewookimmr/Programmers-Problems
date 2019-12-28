def solution(record):
    id = {}
    nick = {}
    line_set = []
    
    for r in record:
        words = r.split(" ")

        # id 딕셔너리 준비 
        if words[1] not in id.keys():
            id[words[1]] = len(id.keys())
            nick[id[words[1]]] = words[2]
      
        # id#, ment_type 리스트들의 리스트 생성 
        if words[0] != "Change":
            ment_type = 0
            if words[0] == "Enter":
                ment_type = 0
                nick[id[words[1]]] = words[2]
            else : 
                ment_type = 1
            
            single_line = [id[words[1]], ment_type]
            line_set.append(single_line)   
        else :
            nick[id[words[1]]] = words[2]  

    # print(line_set)
    # print(nick)
    answer = []
    n = len(line_set)
    for i in range(n):
        s_id = line_set[i][0]
        s_nick = nick[s_id]
        s_ment = ""
        if line_set[i][1] == 0:
            s_ment = "님이 들어왔습니다."
        else :
            s_ment = "님이 나갔습니다."
        s_line = s_nick + s_ment
        answer.append(s_line)

    return answer

def best_solution(record): 
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record : 
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
    
    return answer 

record = ["Enter uid1234 Muzi", \
    "Enter uid4567 Prodo",  "Leave uid1234", \
    "Enter uid1234 Prodo","Change uid4567 Ryan"]

result = best_solution(record)
print(result)

