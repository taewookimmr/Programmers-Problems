def solution(s):
    stack = []
    for c in s:
        if len(stack):
            if stack[-1] == c :
                stack.pop()
            else : 
                stack.append(c)
        else : 
            stack.append(c)
    if len(stack):
        return False
    else :
        return True

s = "baabaa"
result = solution(s)
print(result)