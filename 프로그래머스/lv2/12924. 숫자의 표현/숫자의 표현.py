def solution(n):
    cnt = 0
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 != 0:
                cnt += 1
    answer = cnt        
    return answer