# 사람수는 굉장히 크나 여벌의 체육복을 가져온 학생수는 적을때
def solution(n, lost, reserve):
  s = set(lost) & set(reserve) # 체육복을 도난당했으나 여벌이 있는 학생  set: O(n)
  l = set(lost) - s # 체육복을 도난당했으나 여벌이 없는 학생
  r = set(reserve) - s # 여벌의 옷이 있는 학생

  for x in sorted(r):
    if x - 1 in l:
      l.remove(x - 1)
    elif x + 1 in l:
      l.remove(x + 1)
  return n - len(1)

  #O(nlogn)
