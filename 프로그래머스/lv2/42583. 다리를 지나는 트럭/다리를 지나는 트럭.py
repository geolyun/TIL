from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_truck = 0
    truck = deque(truck_weights)
    bridge = deque([0] * (bridge_length))
    
    while bridge:
        t = bridge.popleft()
        sum_truck -= t
        answer += 1
        
        if truck:
            if sum_truck + truck[0] <= weight:
                sum_truck += truck[0]
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
    
    return answer