def solution(cacheSize, cities):
    answer = 0
    city = []
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        c = i.lower()
        if c in city:
            city.pop(city.index(c))
            city.append(c)
            answer += 1
        else:
            if len(city) == cacheSize:
                city.pop(0)
            city.append(c)
            answer += 5
    return answer