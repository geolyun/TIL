def solution(wallpaper):
    answer = []
    idx = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                idx.append([i, j])
    
    m1 = 10000
    m2 = 10000
    M1 = 0
    M2 = 0
    for i in range(len(idx)):
        if idx[i][0] < m1:
            m1 = idx[i][0]
        if idx[i][1] < m2:
            m2 = idx[i][1]
        if idx[i][0] > M1:
            M1 = idx[i][0]
        if idx[i][1] > M2:
            M2 = idx[i][1]
    answer = [m1, m2, M1+1, M2+1]
    return answer