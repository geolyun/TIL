n = int(input())

dic = {}

for i in range(n):
    key, val = input().split()
    if val == "enter":
        dic[key] = val
    elif val == "leave":
        del dic[key]    

sorted_keys = sorted(dic.keys(), reverse=True)

for key in sorted_keys:
    print(key)