def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    sorted_answer = sorted(answer)
    print(sorted_answer)
    return sorted_answer