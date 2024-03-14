def solution(s, skip, index):
    answer = ''
    for i in s:
        asci = ord(i)
        idx = index
        while idx > 0:
            asci += 1
            if asci > ord('z'):
                asci = ord('a')
            if chr(asci) not in skip:
                idx -= 1
        answer += chr(asci)
    return answer