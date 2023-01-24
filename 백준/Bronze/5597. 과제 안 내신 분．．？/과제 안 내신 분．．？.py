a = [x for x in range(1, 31)]
for _ in range(28):
    a.remove(int(input()))
print(a[0])
print(a[1])