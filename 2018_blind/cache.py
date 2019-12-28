def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5

    queue=[]
    accum = 0
    for city in cities:
        city=city.lower()
        if len(queue)==0:
            queue.append(city)
            accum+=5
        else :
            if city in queue:
                accum+=1
                idx=queue.index(city)
                queue.append(queue.pop(idx)) ## 뒤로 돌린다.
                if len(queue) > cacheSize:
                    queue.pop(0)
            else :
                queue.append(city)
                accum+=5
                if len(queue) > cacheSize:
                    queue.pop(0)
    return accum
            
            