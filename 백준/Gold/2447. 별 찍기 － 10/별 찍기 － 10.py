def solution(n):
    if n == 3:
        return [['***'], ['* *'], ['***']]
    else:
        one, two = [], []
        for i in solution(n // 3):
            one.append(i * 3)
        for i in solution(n // 3):
            two.append(i + [' ' * (n // 3)] + i)
        return one + two + one


for i in solution(int(input())):
    print(''.join(i))