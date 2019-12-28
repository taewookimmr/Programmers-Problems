def solution(n, a, b):
    A = n + a -1 
    B = n + b -1
    count = 0
    while A != B:
        A //=2
        B //=2
        count += 1
    return count


n = 8
a = 4
b = 7
result = solution(n, a, b)
print(result)