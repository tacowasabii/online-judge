n = int(input())

a = n // 5
flag = 0
for i in range(a + 1):
    if (n - (a - i) * 5) % 3 == 0:
        print(a - i + (n - (a - i) * 5) // 3)
        flag = 1
        break
if flag == 0:
    print(-1)
