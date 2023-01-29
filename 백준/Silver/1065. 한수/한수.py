def hansoo(n):
    if n < 100:
        print(n)
    else:
        count = 0
        if n != 1000:
            for i in range(100, n + 1):
                tmp = list(map(int, str(i)))
                if tmp[1] * 2 == tmp[0] + tmp[2]:
                    count += 1
            print(count + 99)
        else:
            for i in range(100, n):
                tmp = list(map(int, str(i)))
                if tmp[1] * 2 == tmp[0] + tmp[2]:
                    count += 1
            print(count + 99)


hansoo(int(input()))