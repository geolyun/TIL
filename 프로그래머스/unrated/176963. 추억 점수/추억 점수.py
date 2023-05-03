def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j] == name[k]:
                    score += yearning[k]
                else:
                    continue
        answer.append(score)
    print(answer)
    return answer