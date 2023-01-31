n = int(input())
count = 1
if n == 1:
    print(1)
while n >= 2:
    a = (1 + count) * count // 2
    if (n - 2) // 6 < a:
        print(count + 1)
        break
    count += 1