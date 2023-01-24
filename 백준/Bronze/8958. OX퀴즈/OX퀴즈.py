n = int(input())
for _ in range(n):
    a = input()
    count = 0
    num = 0
    for i in a:
        if i == 'O':
            num += 1
            count += num
        else:
            num = 0
    print(count)