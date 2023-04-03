arr = []

while True:
    try:
        l = input()
    except EOFError:
        break
    arr.append(l)

for i in arr:
    print(i)