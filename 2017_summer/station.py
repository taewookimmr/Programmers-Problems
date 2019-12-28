def solution(n, stations, w):
    reach = [0 for _ in range(n+1)]
    for s in stations:
        start = max(s-w, 1)
        end = min(n, s+w)
        for i in range(start, end+1):
            reach[i] = 1

    count = 0
    i = 1
    while i <= n:
        if reach[i] == 0 : 
            count += 1
            i += 2*w + 1
        else :
            i += 1
    return count
    


    


n = 11 
stations = [4, 11]
w = 1
result = solution(n, stations, w)
print(result)