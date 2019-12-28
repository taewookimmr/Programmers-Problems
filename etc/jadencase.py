def solution(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = []
    stack=[]
    for w in s:
        if w==" ":
            if len(stack):
                result += stack
                stack.clear()
            result.append(w)
        else :
            if len(stack):
                stack.append(w.lower())
            else :
                if w in alpha:
                    w=w.upper()
                stack.append(w)
    result += stack
    return "".join(result)