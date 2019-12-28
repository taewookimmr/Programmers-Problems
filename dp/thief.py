

# 설명이 안되는데?
def solution(money):
    n = len(money)
    accum = [money[i] for i in range(n)]
    answer = []
    for i in range(n-2):
        n1= (i+2)%n
        n2= (i+3)%n
        if n1 == 0:
            break
        if accum[n1] < accum[i] + money[n1]:
            accum[n1] = accum[i] + money[n1]
        if accum[n2] < accum[i] + money[n2]:
            accum[n2] = accum[i] + money[n2]
    
    accum.pop()
    accum.pop(0)
    answer.append(max(accum))

    accum = [money[i] for i in range(n)]
    for i in range(1, n-1):
        n1= (i+2)%n
        n2= (i+3)%n
        if n1 == 0:
            break
        if accum[n1] < accum[i] + money[n1]:
            accum[n1] = accum[i] + money[n1]
        if accum[n2] < accum[i] + money[n2]:
            accum[n2] = accum[i] + money[n2]
    accum.pop(0)
    answer.append(max(accum))

    return max(answer)
    

money = [1,2,3,1]
result = solution(money)
print(result)

