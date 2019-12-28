def solution(genres, plays):
    dic = {}
    for g, p in zip(genres, plays):
        if g in dic.keys():
            dic[g] += p 
        else :
            dic[g] = p
    
    lst = list(dic.items())
    lst = sorted(lst, key = lambda x: x[1],  reverse = True)
 
    answer = [] 
    for g, _ in lst :
        heap = []
        import heapq
        for i, z in enumerate(zip(genres, plays)):
            if z[0] == g :
                heapq.heappush(heap, [-z[1], i])

        for _ in range(2):
            if len(heap) == 0 : break
            [_, idx] = heapq.heappop(heap)
            answer.append(idx)
    return answer 
            

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))