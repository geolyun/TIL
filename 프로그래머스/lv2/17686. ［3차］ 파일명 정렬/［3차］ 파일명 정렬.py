import re

def solution(files):
    answer = []
    file = []
    
    for idx, word in enumerate(files):
        # 정규표현식 공부 반드시 해야지
        match = re.search(r"(\D+)(\d{1,5})(.*)", word)
        
        head = match.group(1)  # 숫자 이전의 문자열
        number = match.group(2)  # 숫자
        tail = match.group(3)  # 숫자 이후의 나머지
        
        head = head.lower()
        number = int(number)
        
        file.append([head, number, tail, idx])
    file = sorted(file, key = lambda x: (x[0], x[1]))
    
    for i in file:
        answer.append(files[i[-1]])
    return answer