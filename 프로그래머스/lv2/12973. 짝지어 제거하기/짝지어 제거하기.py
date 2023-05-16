def solution(s):
    answer = -1
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer