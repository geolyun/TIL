def solution(prices):
    answer = []
    prices = prices[::-1]
    
    while len(prices) > 0:
        cnt = 0
        n = prices.pop()
        for i in range(len(prices)-1, -1, -1):
            cnt += 1
            if n > prices[i]:
                break
        answer.append(cnt)

    return answer