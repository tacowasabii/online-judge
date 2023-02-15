n = int(input())
for _ in range(n):
    ps = list(input())
    cnt = 0
    flag = 0
    for i in ps:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print('NO')
            flag = 1
            break
    if flag == 0 and cnt != 0:
        print('NO')
    elif flag == 0 and cnt == 0:
        print('YES')