def solution(n, t, m, p):
    answer = ''
    num = ''
    
    def change_binary(number):
        result = ''
        if number == 0 :
            return str(0)
        while number > 0:
            number, mod = divmod(number, n)
            if n > 10 and (10 <= mod <= 15):
                alp_list = ["A", "B", "C", "D", "E", "F"]
                result += alp_list[mod-10]
            else:
                result += str(mod)
        return result[::-1]
    
    s = 0
    while s < t * m:
        num += change_binary(s)
        s += 1
        
    answer = "".join(num[idx] for idx in range(p - 1, t * m, m))
    return answer