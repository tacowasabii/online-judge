def solution(myString):
    ans = ''
    for i in myString:
        if ord(i) < ord('l'):
            ans += 'l'
        else:
            ans += i
    return ans