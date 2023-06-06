def solution(skill, skill_trees):
    answer = 0
    arr = []
    
    # skill의 최대 길이가 크지 않으므로 가능한 스킬트리들을 전부 리스트에 추가했음
    for i in range(len(skill)):
        arr.append(skill[0:i+1])
    
    for i in skill_trees:
        # 스킬트리 리스트를 돌면서 스킬 문자열 안에 있으면 문자열 변수에 추가
        tree = ""
        for j in i:
            if j in skill:
                tree += j
        # 스킬과 관련이 없는 공백 문자열도 가능한 스킬트리
        if tree in arr or len(tree) == 0:
            answer += 1

    return answer