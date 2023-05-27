def solution(want, number, discount):
    answer = 0
    cnt = sum(number)
    
    for i in range(len(discount)-cnt+1):
        # 리스트의 길이가 물품 수와 같을 때까지만 리스트를 만들면 됨
        ord = discount[i:i+cnt]
        cnt_list = []
        for j in want:
            # discount에서 number의 수만큼 뽑은 리스트에서 want에 있는 요소의 개수를 센 뒤 number과 같으면 답에 +1을 해줌
            cnt_list.append(ord.count(j))
        if cnt_list == number:
            answer += 1
    return answer