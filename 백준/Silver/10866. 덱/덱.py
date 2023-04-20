from collections import deque

n = int(input())

deq = deque()
result = []

for i in range(n):
    ord = input()
    if "push_back" in ord:
        deq.append(ord[10:])
    elif "push_front" in ord:
        deq.appendleft(ord[11:])
    elif ord == "pop_front":
        if len(deq) == 0:
            result.append(-1)    
        else:    
            result.append(deq.popleft())
    elif ord == "pop_back":
        if len(deq) == 0:
            result.append(-1)    
        else:    
            result.append(deq.pop())
    elif ord == "size":
        result.append(len(deq))
    elif ord == "empty":
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif ord == "front":
        if len(deq) == 0:
            result.append(-1)    
        else:    
            result.append(deq[0])
    elif ord == "back":
        if len(deq) == 0:
            result.append(-1)    
        else:    
            result.append(deq[-1])

for i in result:
    print(i)