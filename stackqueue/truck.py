def push_left(bridge, new_car = 0):
    popped_right = bridge.pop()
    bridge.insert(0, new_car)
    return bridge


def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    bridge = [0]*bridge_length
    time = 0
    
    while time == 0 or sum(bridge) != 0 :
        # print(time)
        if len(truck_weights) > 0:
            new_car = truck_weights[0]
            if new_car + sum(bridge[:-1]) <= weight:
                bridge = push_left(bridge, new_car = new_car)
                del truck_weights[0]
        else:
            bridge = push_left(bridge, new_car = 0)
        time+=1

    return time





bl = 100 
wt = 100
tw = [10]*10

result = solution(bl, wt, tw)
print(result)