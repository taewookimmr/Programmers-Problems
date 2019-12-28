def solution(dec):
    answer =[]

    parent = (dec-1)//3
    tail = dec % 3
    tail = tail if tail else 4
    answer.append(tail)

    while parent != 0:
        tail = parent % 3
        tail = tail if tail else 4
        answer.append(tail)
        parent = (parent-1)//3
    
    answer = [str(e) for e in answer][::-1]

    return "".join(answer)