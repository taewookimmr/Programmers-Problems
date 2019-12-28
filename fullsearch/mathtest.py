def solution(answers):
    n = len(answers)
    count = [n//5 + 1 , n//8+1,  n//10+1]

    solution = []
    solution.append([1,2,3,4,5]*count[0])
    solution.append([2,1,2,3,2,4,2,5]*count[1])
    solution.append([3,3,1,1,2,2,4,4,5,5]*count[2])

    count = [0]*3
    for i in range(n):
        for j in range(3):
            if solution[j][i] == answers[i]:
                count[j] +=1

    # print(count)
    result = []
    maxim = max(count)
    for i in range(3):
        if count[i] == maxim:
            result.append(i+1)

    return result


answers = [1,3,2,4,2]
result = solution(answers)
print(result)          
    

