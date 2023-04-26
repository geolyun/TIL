def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    for i in range(len(d)):
        if budget - sorted_d[i] >= 0:
            budget = budget - sorted_d[i]
            answer += 1
            print(budget)
        else:
            break

    return answer