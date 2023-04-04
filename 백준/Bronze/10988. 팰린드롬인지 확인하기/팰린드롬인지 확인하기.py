w = input()

for i in range(len(w)//2):
    if w[i] != w[len(w)-1-i]:
        print(0)
        break
else:
    print(1)