def solution(arr):
    answer = 0
    
    for i in range(len(arr)-1):
        # 리스트에서 2개씩 출력해서 최소공배수를 구한 후 다시 리스트에 삽입
        # 리스트 길이가 1이 되면 그때 그 값 출력
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