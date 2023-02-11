def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


a = str(factorial(int(input())))[::-1]
cnt = 0
for i in a:
    if i != '0':
        break
    cnt += 1
print(cnt)