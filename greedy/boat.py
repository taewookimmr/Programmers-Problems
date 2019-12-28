def solution(people, limit):
    n = len(people)
    people.sort(reverse=True)
    lindex = 0
    rindex = n-1
    count = 0
    bount = 0
    while True :
        if  lindex != rindex and people[lindex] + people[rindex] <= limit:
            bount += 1
            lindex +=1
            rindex -=1
        else : 
            count +=1
            lindex +=1
        if  2*bount + count == n:
            break
    return count + bount 



def short_solution(people, limit):
    answer = 0
    poo = sorted(people)
    while poo:
        if len(poo) == 1:
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.pop(0)
            poo.pop()
            answer += 1
    return answer


people = [70, 50, 80, 50]
limit = 100
result = short_solution(people, limit)
print(result)