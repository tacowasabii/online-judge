a = input()
b = set()
for i in range(len(a)):
    for j in range(len(a) - i):
        b.add(a[j:j + i + 1])
print(len(b))