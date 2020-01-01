from itertools import permutations
def solution(arr):
    n = len(arr)
    m = n//2
    idx = [2*e+1 for e in range(m)] 
    arr = [e if i%2 else int(e) for i, e in enumerate(arr)]
    permlist = list(permutations(idx))
    answer = []
    for perm in permlist:
        temp = arr[:]
        n = len(perm)
        j = 0
        while j < n:
            idx = perm[j]
            a = temp[idx-1]
            b = temp[idx+1]
            operation = temp[idx]
            if operation == "+":
                temp = temp[:idx-1]+[a+b]+temp[idx+2:]
            else :
                temp = temp[:idx-1]+[a-b]+temp[idx+2:]
            perm = [e-2 if e > idx else e for e in perm]
            j+= 1
        answer.append(temp[0])

    print(answer)
    return max(answer)


arr =["1", "-", "3", "+", "5", "-", "8"]
result=solution(arr)
print(result)