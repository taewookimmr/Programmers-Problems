def solution(h):
    a = [0]
    for i in range(1, len(h)):
        count = 0
        for j in range(i-1, -1, -1):
            if h[j] > h[i]:
                a.append(j+1)
                count = 1
                break
        if count == 0 : 
            a.append(0)
    print(a)

def best_solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans


h = [6,9,5,7,4]
result = best_solution(h)
print(result)