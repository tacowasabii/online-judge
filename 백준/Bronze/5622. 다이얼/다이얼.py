s = input()
count = 0
for i in s:
    count += (ord(i) - ord('A')) // 3 + 3
    if i == 'S' or i == 'V' or i == 'Y' or i == 'Z':
        count -= 1
print(count)