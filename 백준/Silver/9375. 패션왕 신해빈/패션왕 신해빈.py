n = int(input())
for _ in range(n):
    nn = int(input())
    clothes = {}
    for _ in range(nn):
        name, kind = input().split()
        clothes[kind] = clothes.get(kind, 0) + 1
    a = [v for k, v in clothes.items()]
    ans = 1
    for i in a:
        ans *= (i + 1)
    print(ans - 1)