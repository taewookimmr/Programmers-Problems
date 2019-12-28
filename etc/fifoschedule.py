def solution(n, cores):
    m = len(cores)
    available = [0 for _ in range(m)]
    while True:
        for i, core in enumerate(cores):
            if available[i]==0:
                available[i] = core
                n-=1
                if n==0:
                    return i+1
        available = [e-1 for e in available]