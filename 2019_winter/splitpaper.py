def solution(w,h):
    import math
    
    if w==h:
        return w*(w-1)
    else :
        if h < w:
            t = w
            w = h 
            h =t 
        # 여기 왔으면 무조건 h > w
        
        def func(a,b):
            
            if a < b:
                t = a
                a = b
                b = t
            if b==0:
                return a
            return /
        return w*h - func(h,w)