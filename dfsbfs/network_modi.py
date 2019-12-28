# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 
# 정보를 교환할 수 있습니다. 
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
    
def solution(n, computers):
    not_visited = [e for e in range(n)]
    check = [0] * n
    count = 0

    def search(index, computers):
        n = len(check)
        if check[index] == 0:
            not_visited.remove(index)
        check[index] = 1
    
        for j in range(n):
            if computers[index][j] == 1:
                if check[j] == 0: #미방문이라면 
                    check[j] = 1
                    not_visited.remove(j)
                    search(j, computers)

    while sum(check) != n:
        search(not_visited[0], computers)
        count += 1
    return count 


computers = [[1,1,0], [1,1,0], [0,0,1]]
n = 3
result = solution(n, computers)
print(result)

