def solution(p):
    
    if len(p) == 0:
        return ""

    def check(src):
        temp = src[:]
        stack =[]
        for t in temp:
            if t == "(":
                stack.append(1)
            else :
                if len(stack):
                    stack.pop()
                else:
                    return False
        return True
    
    def recursive(src):
        countl = 0
        countr = 0
        cutindex = 0
        for i, c in enumerate(src):
            if c == "(":
                countl+=1
            else : 
                countr+=1
            if countl == countr :
                cutindex = i
                break
        u =""
        v =""
        if cutindex == len(src) - 1: # 더 분리가 불가능합니다
            u = src
            v = ""
        else : #분리가 되었습니다.
            u = src[:cutindex+1]
            v = src[cutindex+1:]
            
        if (check(u)):
            # u is correct
            if len(v):
                return  u + recursive(v)
            else:
                return u
        else:
            # u is not correst
            kakao = "(" + recursive(v) + ")" 
            kakaotexi = u[1:-1]
            kakaotexi = "".join(["(" if e == ")" else ")" for e in kakaotexi])
            kakao += kakaotexi
            return kakao
                
                
    if check(p):
        return p            
    return recursive(p)

p = "()))((()"
result = solution(p)
print(result)