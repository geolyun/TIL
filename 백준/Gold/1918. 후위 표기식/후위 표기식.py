n = input()

stack = []
sem = []

for i in n:
    if i.isalpha():
        stack.append(i)
    else:
        if i == "(":
            sem.append(i)
        elif i == ")":
            while sem and sem[-1] != "(":
                stack.append(sem.pop())
            sem.pop()

        elif i == "*" or i == "/":
            while sem and (sem[-1]=="*" or sem[-1]=="/"):
                stack.append(sem.pop())
            sem.append(i)
        
        elif i == "+" or i == "-":
            while sem and sem[-1] != "(":
                stack.append(sem.pop())
            sem.append(i)

while len(sem) > 0:
    stack.append(sem.pop())

for i in range(len(stack)):
    print(stack[i], end='')