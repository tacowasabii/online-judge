n = int(input())
str = input()
ans = 0
for i in range(len(str)):
    ans += (ord(str[i]) - 96) * 31 ** i

print(ans % 1234567891)