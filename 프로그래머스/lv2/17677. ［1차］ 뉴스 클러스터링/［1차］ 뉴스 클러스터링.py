def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    hap = []
    gyo = []
    J = 0
    
    for i in range(len(str1)-1):
        s = str1[i] + str1[i+1]
        s = s.upper()
        if "A" <= s[0] <= "Z" and "A" <= s[1] <= "Z":
            # 영문자로 된 글자 쌍만 유효
            s1.append(s)
    
    for i in range(len(str2)-1):
        s = str2[i] + str2[i+1]
        s = s.upper()
        if "A" <= s[0] <= "Z" and "A" <= s[1] <= "Z":
            # 영문자로 된 글자 쌍만 유효
            s2.append(s)

    for i in s1:
        if i not in s2:
            continue
        elif i in gyo:
            continue
        else:
            # 두 리스트 중 더 적은 갯수를 가지고 잇는 원소의 갯수만큼 추가
            m = min(s1.count(i), s2.count(i))
            for j in range(m):
                gyo.append(i)

    for i in s1:
        if i not in s2:
            # 합집합은 str2에는 없고 str1에만 있는 값도 추가해야함
            hap.append(i)
        elif i in hap:
            continue
        else:
            # 두 리스트 중 더 많은 갯수를 가지고 잇는 원소의 갯수만큼 추가
            m = max(s1.count(i), s2.count(i))
            for j in range(m):
                hap.append(i)
    
    # 마찬가지로 str2에는 있는데 str1에는 없는 값도 추가해야함
    for i in s2:
        if i not in s1:
            hap.append(i)
    
    if len(s1) == 0 and len(s2) == 0:
        J = 1
    else:
        J = len(gyo) / len(hap)
        
    answer = int(J * 65536)
    print(gyo, hap)
    return answer