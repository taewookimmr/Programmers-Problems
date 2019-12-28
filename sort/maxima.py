# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
from operator import itemgetter
def solution(numbers):
    n = len(numbers)
    a = list(map(lambda x: " ".join(x).split(), list(map(str, numbers))))
    a.sort(reverse=True)
    print(a)
    

# JichangJang님의 코드를 보며 공부하였습니다.

def compare_value(first, second):
    if len(str(first)) == len(str(second)):
        if first > second:
            return first
        else:
            return second
    else:
        if int(str(first) + str(second)) >= int(str(second) + str(first)):
            return first
        return second


def my_quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        less = []
        same = []
        bigger = []
        for i in numbers:
            if i == numbers[0]:
                same.append(i)
            elif compare_value(i, numbers[0]) == numbers[0]:
                bigger.append(i)
            else:
                less.append(i)
        return my_quick_sort(less) + same + my_quick_sort(bigger)


def mid_solution(numbers):
    for j in numbers:
        if j != 0:
            answer = my_quick_sort(numbers)
            str_answer = ""
            for i in answer:
                str_answer = str_answer + str(i)
            return str_answer
        else:
            pass
    return "0"  

def best_solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse =True)
    print(numbers)
    return str(int(''.join(numbers)))    



numbers = [3, 30, 34, 5, 9]
result = best_solution(numbers)
print(result)