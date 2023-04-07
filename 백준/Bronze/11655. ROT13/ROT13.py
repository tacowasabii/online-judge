s = input()
ans = ''
for i in s:
    if 97 <= ord(i) <= 122:
        ans += chr(97 + (ord(i) - 97 + 13) % 26)
    elif 65 <= ord(i) <= 90:
        ans += chr(65 + (ord(i) - 65 + 13) % 26)
    else:
        ans += i
print(ans)