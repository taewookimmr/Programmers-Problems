def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    time=0
    while len(bridge) != 0:
        time+=1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time



bl = 100 
wt = 100
tw = [10]*10

result = solution(bl, wt, tw)
print(result)