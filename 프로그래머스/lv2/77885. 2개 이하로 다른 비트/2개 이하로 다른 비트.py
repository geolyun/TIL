def solution(numbers):
    answer = []
    # 짝수라면 가장 뒤에 있는 0을 1로 바꾸어주면 조건을 만족함
    # 홀수라면 가장 뒤에 있는 0을 1로 바꾸고 그 다음 인덱스를 0으로 바꾸어주면 조건을 만족함
    # 규칙을 찾으면 쉽게 풀렸음
    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = "1"
    
        if number % 2 == 1:
            bin_number[idx+1] = "0"
        
        answer.append(int(''.join(bin_number), 2))
    return answer