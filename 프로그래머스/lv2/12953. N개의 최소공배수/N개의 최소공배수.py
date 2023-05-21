def solution(arr):
    answer = 0
    
    for i in range(len(arr)-1):
        a = arr.pop()
        b = arr.pop()
        ab = a*b
        tmp = a % b
        while tmp != 0:
            a = b
            b = tmp
            tmp = a % b
        arr.append(int(ab / b))
    
    answer = arr[-1]
    return answer