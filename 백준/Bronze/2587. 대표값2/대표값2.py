temp = []
for _ in range(5):
    temp.append(int(input()))
temp.sort()

print(sum(temp)//5)
print(temp[2])