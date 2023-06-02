def solution(prices):
    answer = []
    prices = prices[::-1]
    
    while len(prices) > 0:
        cnt = 0
        # list의 pop(0)의 시간복잡도는 O(n)이어서 O(1)의 시간복잡도를 가지는 pop(-1) 또는 pop()로 풀어야했음
        n = prices.pop()
        for i in range(len(prices)-1, -1, -1):
            cnt += 1
            if n > prices[i]:
                break
        answer.append(cnt)

    return answer