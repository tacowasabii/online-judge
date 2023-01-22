def solution(s):
    a = s.split(" ")

    for x, i in enumerate(a):
        if i != "":
            a[x] = i[0].upper() + i[1:].lower()
        else:
            a[x] = ""
    return ' '.join(a)