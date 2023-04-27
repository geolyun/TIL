def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif 65 <= ord(i) + n <= 90 and 65 <= ord(i) < 90:
            answer += chr(ord(i) + n)
        elif 97 <= ord(i) + n <= 122 and 97 <= ord(i) <= 122:
            answer += chr(ord(i) + n)
        else:
            answer += chr(ord(i) + n -26)
    return answer