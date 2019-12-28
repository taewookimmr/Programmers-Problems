def solution(routes):
    routes.sort(reverse=True)
    length = len(routes)
    count = 0 
    cam = [0] * length
    camera = 0 
    for i in range(0, length):
        if cam[i] == 0:
            camera=routes[i][0]
            count +=1
        for j in range(i, length):
            if cam[j] == 0 and routes[j][1] >= camera:
                cam[j] = 1
    return count

def best_solution(routes):
    routes = sorted(routes, key = lambda x: x[1])
    last_camera = -300000
    answer = 0
    for route in routes:
        if last_camera < route[0]:
            answer +=1 
            last_camera = route[1]
    return answer 
        


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
result = best_solution(routes)
print(result)