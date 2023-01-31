n = int(input())
count = 1
while True:
    a = (1 + count) * count // 2
    if n <= a:
        break
    count += 1

a = n - (count - 1) * count // 2

if count % 2 == 1:
    top = a
    bot = count + 1 - a
else:
    top = count + 1 - a
    bot = a

print("{}/{}".format(bot, top))