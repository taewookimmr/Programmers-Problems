## 미완성 

def solution(N, number):
    for i in range(1,9):
        if int(str(N)*i) == number:
            return True

    from itertools import combinations as cmb
    operator = ["+","-","*","/"]

    def gen(x):
        result = []
        def recur(accum):
            if len(accum)<x:
                for op in operator:
                    recur(accum+op)
            else:
                result.append(accum)
        recur("")
        return result

    opdupperm = [-1]
    for i in range(1,9):
        opdupperm.append(gen(i))

    def calc(src):
        return 0
    
    queue=[]
    for n in range(1,9):
        for m in range(0,n):
            ## n은 N의 개수, m은 연산자의 개수
            k = 2*n-1
            emptyspace = [e for e in range(1,k,2)]
            possiblecombi = (list(cmb(emptyspace, m)))
            for combi in possiblecombi:
                f = len(combi)
                if f: #연산자 넣을 자리가 한 자리 라도 있으면 
                    for opd in opdupperm[f] :
                        kakao = ["" if e%2 else str(N) for e in range(2*n-1)]
                        i = 0
                        for index in combi:
                            kakao[index] = opd[i]
                            i+=1
                        kakao="".join(kakao)
                        print(kakao)
                        if calc(kakao):
                            return True
    return False
                    
            
N = 5
number = 55
print(solution(N, number))