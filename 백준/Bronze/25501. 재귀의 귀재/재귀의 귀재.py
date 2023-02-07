def recursion(s, l, r, count):
    count += 1
    if l >= r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        return recursion(s, l + 1, r - 1, count)


def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s) - 1, count)


n = int(input())
for _ in range(n):
    a, b = isPalindrome(input())
    print(a, b)