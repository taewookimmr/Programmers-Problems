# 문제 설명

# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
# 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항

# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다

# 오일러 경로
# 그래프의 모든 간선을 정확히 한 번씩 지나는 경로를 말한다.
# u=v 
# 진입 차수와 진출 차수가 같다. 

# u != v
# 시작점과 도착점을 제외한 모든 정점은 반드시 진입 차수와 진출 차수의 값이 같다. 
# 시작점은 진출 차수가 진입 차수보다 하나 더 많아야 하며
# 종료점은 진입 차수가 진출 차수보다 하나 더 많다. 


def solution(tickets):
   
    dic = {}
    index = 0
    for t in tickets:
        for v in t:
            if v not in dic.keys():
                dic[v] = index 
                index += 1
    index = 0
    l = list(dic.keys())
    a = l[0]
    sorted_keys_list = l[1:]
    sorted_keys_list.sort()
    sorted_keys_list.insert(0, a)
    dic.clear()
    index = 0
    for k in sorted_keys_list:
        dic[k] = index
        index+=1

    # 인접 그래프 생성
    n = len(dic)
    g = [[0 for x in range(n)] for y in range(n)]
    for t in tickets:
        start = dic[t[0]]
        end   = dic[t[1]]
        g[start][end] += 1
    print(g)

    answer = []
    def dfs(u):
        for v in range(n):
            while g[u][v] > 0:
                g[u][v] -=1
                dfs(v)
        answer.append(u)  
    dfs(0)
    answer.reverse()
    result = []
    for i in range(len(answer)):
        result.append(sorted_keys_list[answer[i]])

    s = 0
    for gr in g:
        s+= sum(gr)
    if s != 0 :
        return []
    return result
 

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"], ["SFO", "XXX"], ["ICN", "YYY"]]
result = solution(tickets)
print(result)