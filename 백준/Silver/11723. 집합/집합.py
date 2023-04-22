import sys

input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    a = input().strip()
    if a == 'all':
        s = set(i for i in range(1, 21))  # 숫자를 int 타입으로 처리하도록 변경
    elif a == 'empty':
        s = set()
    else:
        b, c = a.split()
        c = int(c)  # 숫자를 int 타입으로 처리하도록 변경
        if b == 'add':
            s.add(c)
        elif b == 'remove':
            try:  # try-except를 사용하여 예외 처리
                s.remove(c)
            except KeyError:
                continue
        elif b == 'check':
            if c in s:
                print(1)
            else:
                print(0)
        elif b == 'toggle':
            if c in s:
                s.remove(c)
            else:
                s.add(c)