n = int(input())
count = 0
a = n
while True:
    a = int(str(a)[-1] + str(sum(map(int, list(str(a)))))[-1])
    count += 1
    if a == n:
        break
print(count)