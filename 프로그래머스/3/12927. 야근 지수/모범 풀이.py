def noOvertime(n, works):
  if n>=sum(works):
    return 0;

  while n > 0:
    works[works.index(max(works))] -= 1
    n -= 1

  result = sum([w ** 2 for w in works])

  return result