def solution(priorities, location):
    answer = 0
    stack = []
    idx = [i for i in range(len(priorities))]
    
    while len(priorities) > 0:
        # priorities의 길이가 0이 될 때까지 반복
        # 같게되면 결과 리스트에 인덱스를 추가하고 스택에서 꺼내주면 됨
        m = max(priorities)
        if priorities[0] == m:
            stack.append(idx[0])
            priorities.pop(0)
            idx.pop(0)
        else:
            # priorities의 맨앞 요소가 최댓값일때 까지 맨앞 요소를 맨뒤에 추가하는 식으로 반복
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
        
    answer = stack.index(location) + 1
    return answer