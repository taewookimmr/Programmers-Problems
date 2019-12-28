def get_strike_ball(input, problem):
    s_count = 0
    b_count = 0
    n = len(input)
    for i in range(n):
        for j in range(n):
            if problem[i] == input[j]:
                if i != j :
                    b_count += 1
                else :
                    s_count += 1
    return s_count, b_count 

def get_sepa(input):
    result = []
    while input != 0:
        a = input % 10
        result.append(a)
        input = input // 10
    result.reverse()
    # print(result)
    return result 

def solution(baseball):
    n = len(baseball)
    result = 0
    for i in range(1, 9+1):
        m = list(range(1, 9+1))
        m.remove(i)
        for j in m:
            l = list(range(1, 9+1))
            l.remove(i)
            l.remove(j)
            for k in l:
                input = [i,j,k]
                # print(i,j,k)
                count = 0
                for z in range(n):
                    problem = get_sepa(baseball[z][0])
                    s, b = get_strike_ball(input, problem)
                    if s == baseball[z][1] and b == baseball[z][2]:
                        count += 1
                if count == n:
                    result += 1
    # print(result)
    return result 
                
    
    



baseball = []
baseball.append([123,1,1])
baseball.append([356,1,0])
baseball.append([327,2,0])
baseball.append([489,0,1])

solution(baseball)