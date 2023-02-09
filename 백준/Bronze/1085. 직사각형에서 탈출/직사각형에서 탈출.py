x, y, w, h = map(int, input().split())
print(min(abs(y - h), abs(y), abs(x - w), abs(x)))