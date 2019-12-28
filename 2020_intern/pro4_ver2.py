def solution_ver2(k, room_number):
    check = [0 for _ in range(k+1)]
    p = len(room_number)
    result= []
    
    for want in room_number:
        if check[want] == 0:
            result.append(want)
            check[want]=1
        else : 
            for j in range(want,k+1):
                if check[j]==0:
                    result.append(j)
                    check[j]=1
                    break
    return result
