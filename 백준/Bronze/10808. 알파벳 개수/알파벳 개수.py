s = input()

alp = {}
for i in range(97, 123):
    alp[i] = 0
for i in s:
    alp[ord(i)] += 1
for v in alp.values():
    print(v, end=' ')