def solution(k, room_number):
    check = [0 for _ in range(k+1)]
    p = len(room_number)
    result= [0 for _ in range(p)]
    
    for i,want in enumerate(room_number):
        if check[want] == 0:
            result[i] = want
            check[want]=1
        else : 
            testcheck = check[want:]
            emptyindex=0
            if testcheck.count(0) !=0:
                emptyindex = testcheck.index(0)
            alterroom = want + emptyindex
            
            result[i]=alterroom
            check[alterroom]=1
    return result
            