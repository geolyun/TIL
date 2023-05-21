def solution(s):
    answer = 0
    s = list(s)
    cnt = 0
    
    while cnt < len(s):
        stack = []
        check = True
        s.append(s.pop(0))
        for i in range(len(s)):
            if len(stack) == 0 and s[i] in (")", "}", "]"):
                check = False
                break
            elif s[i] == "(":
                stack.append("(")
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
            elif s[i] == "{":
                stack.append("{")
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()
            elif s[i] == "[":
                stack.append("[")
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop()

        if len(stack) == 0 and check == True:
            answer += 1
        cnt += 1

    return answer