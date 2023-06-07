def solution(numbers):
    # 스택을 이용해서 푸는 문제
    # 중요할 때 다시 한번 풀기
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer