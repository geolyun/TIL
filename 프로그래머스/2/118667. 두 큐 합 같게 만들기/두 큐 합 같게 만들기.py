from collections import deque


def solution(queue1, queue2):

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    target = (sq1 + sq2) // 2
    
    if sq1+sq2 % 2 == 1:
        return -1
    
    result = 0
    limit = len(queue1)*3 + len(queue2)
    
    while sq1 != sq2:
        if result >= limit:
            return -1
        else:
            if sq1 > target:
                q1 = queue1.popleft()
                queue2.append(q1)
                sq1 = sq1 - q1
                sq2 = sq2 + q1
                result += 1
            elif sq2 > target:
                q2 = queue2.popleft()
                queue1.append(q2)
                sq1 = sq1 + q2
                sq2 = sq2 - q2
                result += 1
            elif sq2 == sq1 == target:
                break
    return result