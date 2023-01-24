def solution(s):
    a = s.split(' ')
    for i in range(len(a)):
        if a[i] != '':
            k = list(a[i])
            for j in range(len(k)):
                if j % 2 == 0:
                    k[j] = k[j].upper()
                else:
                    k[j] = k[j].lower()
            a[i] = ''.join(k)
    return ' '.join(a)