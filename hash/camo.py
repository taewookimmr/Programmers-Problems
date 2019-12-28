def solution(clothes):
    dic = {}
    for e in clothes:
        category = e[1]
        name = e[0]
        if category in dic.keys():
            dic[category] += 1
        else :
            dic[category] = 1

    answer = 1
    for e in dic.keys():
        answer *= (dic[e] + 1)
    return answer - 1


def solution_other(clothes):
    from collections import Counter 
    from functools import reduce 
    cnt = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y : x*(y+1), cnt.values(), 1)-1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)