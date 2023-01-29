s = input().lower()
a = {}
for i in s:
    a[i] = a.get(i, 0) + 1

values = [v for k, v in a.items()]
if values.count(max(values)) > 1:
    print('?')
else:
    print(''.join([k for k, v in a.items() if v == max(values)]).upper())