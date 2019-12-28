def solution(brown, red):
    answer = []

    for w in range(red, red//2-1, -1):
        h = red // w
        if w * h == red :
            sum = 2*(w+h) + 4
            if sum == brown:
                answer.append(w+2)
                answer.append(h+2)
                break


    return answer 


def best_solution(brown, red):
    for i in range(1, int(red**(1/2)+1)):
        if red % i == 0:
            if 2*(i + red//i) + 4 == brown:
                return [red//i+2, i+2]

brown = 10
red = 2 
getit = best_solution(10, 2)
print(getit)

