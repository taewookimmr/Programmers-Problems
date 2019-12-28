
def solution(number, k):
    n = len(number)
    w = n-k
    update = 1
    answer = []
    mask = []

    while w != 0:
        print(w)
        if update == 1:
            n_set = set(number)
            update = 0
        m_set = set([])
        del_set = n_set-m_set
        while True :
            max_index, mx = 0,0
            if len(del_set):
                max_index, mx = number.index(max(del_set)), max(del_set)
            else : 
                break
            if k >= max_index:
                break
            else : 
                m_set.add(mx)
                del_set = n_set-m_set

        k -= max_index
        if k != 0:
            answer.append(mx)
            number = number[max_index+1:]
            w-=1
            if mx not in number :
                update = 1
        else :
            answer += number[max_index:]
            break
    
    return "".join(answer)
        

def short_solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -=1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "4177252841"
k = 4
result = short_solution(number,k)
print(result)