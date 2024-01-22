def solution(sequence, k):
    answer = []
    S = 0
    e = len(sequence)-1
    
    for i, j in enumerate(sequence[::-1]):
        S += j
        if S < k:
            pass
        elif S > k:
            S -= sequence[e]
            e -= 1
            if S == k:
                answer.append([len(sequence)-i-1, e])

        else:
            answer.append([len(sequence)-i-1, e])
    
    answer.sort(key=lambda x : (x[1]-x[0], x[0]))
    # print(answer)
    return answer[0]