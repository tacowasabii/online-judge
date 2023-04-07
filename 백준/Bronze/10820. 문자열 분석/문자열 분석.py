while True:
    ans = [0, 0, 0, 0]
    try:
        s = input()
        for i in s:
            if i == " ":
                ans[3] += 1
            elif 97 <= ord(i) <= 122:
                ans[0] += 1
            elif 65 <= ord(i) <= 90:
                ans[1] += 1
            else:
                ans[2] += 1
        print(*ans)
    except EOFError:
        break