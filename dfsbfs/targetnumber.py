# n개의 음이 아닌 정수가 있다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들고자 한다.
# 예를 들어 [1,1,1,1,1,]로 숫자 3을 만들려면 다음 다섯 방법
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

def recursive(numbers, index, pre_sum, answer):
    if index < len(numbers):
        recursive(numbers, index+1, pre_sum+numbers[index], answer)
        recursive(numbers, index+1, pre_sum-numbers[index], answer)
    else :
        answer.append(pre_sum)

def solution(numbers, target):
    answer = []
    count = 0
    recursive(numbers, 0, 0, answer)
    for i in answer:
        if i == target :
            count += 1
    return count


def best_solution(numbers, target):
    if not numbers and target == 0:
        # numbers가 비어 있고, target도 0이 되었을 때
        return 1
    elif not numbers:
        # numbers가 비어 있고, target이 0이 되지 않았을 때
        return 0
    else :
        # numbers가 비어 있지 않고 
        return best_solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

numbers = [1,1,1,1,1]
target = 3
result = best_solution(numbers, target)
print(result)