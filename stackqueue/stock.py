def solution(prices):
    n = len(prices)
    answer = []
    
    for i in range(n-1):
        count = 0
        break_count = 0
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                count += 1
            else :
                count += 1
                break
        answer.append(count)
    answer.append(0)
    return answer


def best_solution(prices):
    n = len(prices)
    answer = [0] * len(prices)
    for i in range(n):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break 
prices = [1,2,3,2,3]
result = solution(prices)
print(result)