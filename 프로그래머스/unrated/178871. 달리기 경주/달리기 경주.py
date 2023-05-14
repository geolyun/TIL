def solution(players, callings):
    a = {}
    for index, value in enumerate(players):
        a[value] = index
        
    for name in callings:
        pre, back = a[name]-1, a[name]
        players[pre], players[back] = players[back], players[pre]
        a[players[pre]], a[players[back]] = a[players[pre]] -1, a[players[back]] +1
        
    return players