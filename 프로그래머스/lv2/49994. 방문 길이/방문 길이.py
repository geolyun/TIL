def solution(dirs):
    answer = 0
    
    x, y = 0, 0
    loc = [(x, y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in dirs:    
        if i == "U":
            nx = x + dx[3]
            ny = y + dy[3]
        elif i == "D":
            nx = x + dx[2]
            ny = y + dy[2]
        elif i == "R":
            nx = x + dx[1]
            ny = y + dy[1]
        elif i == "L":
            nx = x + dx[0]
            ny = y + dy[0]
        if not -5 <= nx <= 5 or not -5 <= ny <= 5:
            continue
        else:
            e = (x, y, nx, ny)
            shift = 2
            shifted_tuple = e[-shift:] + e[:-shift]
            if shifted_tuple in loc:
                x, y = nx, ny
            else:
                loc.append(e)
                x, y = nx, ny
    
    sloc = list(set(loc))
    answer = len(sloc) - 1
    return answer