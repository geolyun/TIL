def solution(k, score):
    answer = []
    queue = []
    
    for i in range(len(score)):
        queue.append(score[i])
        queue = sorted(queue, reverse = True)
        
        if len(queue) > k:
            queue.pop()
        answer.append(queue[-1])

    print(answer)
    return answer