def solution(keymap, targets):
    answer = []
    for i in targets:
        cnt = 0
        
        for j in i: # 타겟의 문자열 하나씩 나눔
            check = False # 목표 문자열을 작성할 수 있는지 여부
            idx = 101
            for key in keymap:
                if j in key:
                    idx = min(key.index(j)+1, idx) # keymap을 도는 동안 목표 문자열의 인덱스가 더 작은 값으로 그때마다 변경
                    check = True # 목표 문자열을 작성할 수 있음
            
            if check == False: # 목표 문자열을 작성할 수 없으면 리스트에 담을 값을 -1로 설정
                cnt = -1
                break
        
            cnt += idx # 타겟의 문자열 하나하나의 인덱스를 결과값에 더함
        
        answer.append(cnt) # 정답에 추가함
    
    return answer