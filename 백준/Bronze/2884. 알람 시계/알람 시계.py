h, m = map(int, input().split())

if m< 45:
    h-=1
    if h<0:
        h+=24
m = (m + 15) % 60

print(h, m)