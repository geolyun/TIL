l = list(input())

stack = []
result = 0
 
for i in range(len(l)):
    if l[i] == "(":
        stack.append(l[i])
    elif l[i] == ")":
        stack.pop()
        if l[i-1] == "(":
            result += len(stack)
        elif l[i-1] == ")":
            result += 1    

print(result)        