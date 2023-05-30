from collections import deque

def solution(numbers, target):
    answer = 0
    que = deque([(0,0)])
    while que:
        n, l = que.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and n == target:
            answer += 1
        que.append((n+numbers[l-1], l+1))
        que.append((n-numbers[l-1], l+1))
    return answer