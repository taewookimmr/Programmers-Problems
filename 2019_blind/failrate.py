def solution(N, stages):
    #N은 스테이지의 개수

    m = len(stages)
    source=[[0,0,0] for _ in range(N+1)]
    fail=[0.0 for _ in range(N+1)]
    
    for s in range(1, N+1):
        for stage in stages:
            if s <= stage :
                source[s][0] += 1
            if s == stage :
                source[s][1] += 1
        if source[s][0] != 0:
            fail[s]= float(source[s][1]/source[s][0])
    
    fail[0] = -1
    answer = list(enumerate(fail))
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    answer = [e[0] for e in answer][:-1]
    return answer
    # answer = []
    # while len(answer) != N:
    #     idx = fail.index( max(fail))
    #     fail[idx] = -1
    #     answer.append(idx)
        
    #return answer