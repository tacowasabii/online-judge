def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] != ' ':
            if ord(s[i]) <= 90:
                s[i] = chr((ord(s[i]) + n - 65) % 26 + 65)
            else:
                s[i] = chr((ord(s[i]) + n - 97) % 26 + 97)
    return ''.join(s)