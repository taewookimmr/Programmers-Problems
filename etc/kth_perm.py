def solution(n,k):
    # 1부터 n까지의 자연수로 구성된 집합
    # 이 집합의 permutations를 오름차순으로 정렬할 때
    # k번째 permutation를 반환하는 함수를 작성하여라
    from math import factorial as facto
    
    pool = [e+1 for e in range(n)]
    result = []
    f = facto(n)
    
    k-=1
    while n>0:
        f //= n 
        n-=1
        result.append(pool.pop(k//f))
        k %= f

    return result


