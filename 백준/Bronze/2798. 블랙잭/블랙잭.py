n, m = map(int, input().split())
cards = list(map(int, input().split()))

max = 0
for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            sum = cards[i] + cards[j] + cards[k]
            if max < sum <= m:
                max = sum
print(max)