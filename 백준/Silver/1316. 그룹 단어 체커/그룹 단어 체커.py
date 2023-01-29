n = int(input())
count = 0
for _ in range(n):
    s = input()
    temp = ''
    a = []
    for i in s:
        if i != temp and i in a:
            count -= 1
            break
        elif i != temp and i not in a:
            a.append(i)
        temp = i
    count += 1
print(count)