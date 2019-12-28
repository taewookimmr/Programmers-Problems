def solution(array, commands):
    n = len(commands)
    answer = []
    for i in range(n):
        s = commands[i][0]
        e = commands[i][1]
        temp = array[s-1:e]
        temp = sorted(temp)
        m = commands[i][2]
        answer.append(temp[m-1])

    return answer 


def best_solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]

result = solution(array, commands)
print(result)