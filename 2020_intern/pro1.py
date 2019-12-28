def solution(board, moves):
    n = len(board)
    slots = [[] for _ in range(n+1)]
    for row in board:
        for i in range(n):
            if row[i]:
                slots[i+1].append(row[i])
    
    stack = []
    count = 0
    # slots내 slot의 앞 인덱스에 높은 곳 인형이 있다.
    for move in moves:
        #move는 slot넘버를 뜻한다.
        if len(slots[move]):
            ready = slots[move].pop(0)
            if len(stack) == 0:
                stack.append(ready)
            else : 
                top=stack[-1]
                if top == ready :
                    stack.pop()
                    count +=1
                else:
                    stack.append(ready)
    return count*2
                    
                