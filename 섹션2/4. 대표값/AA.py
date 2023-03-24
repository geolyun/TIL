N = int(input())
s = list(map(int, input().split()))

avg = round(sum(s)/N)

min = float('inf')
for idx, x in enumerate(s):
    tmp = abs(avg-x)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp==min:
        if x > score:
            score = x
            res=idx+1

print(avg, res)

#arr = [5, 3, 7, 9, 2, 5, 2, 6]
#arrMin = float('inf')
#for i in range(len(arr)):
    #if arr[i]<arrMin:
        #arrMin=arr[i]     

#print(arrMin)