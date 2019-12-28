def solution(stock, dates, supplies, k):
    mystock = stock
    count = 0
    chunk = list(zip(dates, supplies))
    import heapq
    while  mystock < k:
        count+=1
        pack = []
        temp = []
        for d,s in chunk:
            if d <= mystock:
                heapq.heappush(pack, -s)
            else : 
                temp.append([d,s])
        trump = temp 
        if len(pack):
            mystock += -heapq.heappop(pack)
    return count


stock = 4
dates = [4,10,15]
supplies = [20,5,10]
k = 30
result = solution(stock, dates, supplies, k)
print(result)