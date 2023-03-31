def Count(a):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > a:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

m, n = map(int, input().split())

music = list(map(int, input().split()))

lt = 1
rt = sum(music)


while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) <= n:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)