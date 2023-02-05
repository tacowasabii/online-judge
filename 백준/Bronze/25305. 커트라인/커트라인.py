n, k = map(int, input().split())
temp = list(map(int, input().split()))
temp.sort(reverse=True)
print(temp[k - 1])