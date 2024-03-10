def solution(myString, pat):
    str = ''
    for i in myString:
        if i == 'A':
            str += 'B'
        else:
            str += 'A'
    return int(pat in str)