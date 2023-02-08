n = int(input())

flag = 0
for i in range(1, n):
    i_str = str(i)
    for j in i_str:
        i += int(j)
    if i == n:
        print(int(i_str))
        flag = 1
        break

if flag == 0:
    print(0)