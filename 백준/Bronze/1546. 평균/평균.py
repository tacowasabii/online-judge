n = int(input())
a = list(map(int, input().split()))
b = [x / max(a) * 100 for x in a]
print(sum(b) / n)