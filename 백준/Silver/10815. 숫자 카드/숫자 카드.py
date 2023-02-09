n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())
a = set(a)
for i in b:
    if i in a:
        print(1, end=' ')
    else:
        print(0, end=' ')