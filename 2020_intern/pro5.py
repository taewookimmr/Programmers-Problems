def solution(stones, k):
    kakao = max(stones)
    left=0
    right= kakao
    answer = []
    while left<right:
        mid = int((left+right)//2)
        if mid in answer:
            return mid
        answer.append(mid)
        stack=[]
        con = 0
        for s in stones:
            if s < mid:
                stack.append(s)
            else:
                if len(stack) >= k:
                    ## 못 건너간다.
                    con=1
                    break
                else:
                    stack.clear()
        if con==1:
            right= mid
        else :
            left = mid
            
    return mid
            