def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 1. numbers의 원소들을 문자열로 변환한다.
# 2. 문자열로 변환된 numbers를 3을 곱한 값으로 정렬한다.
# 3. 정렬된 numbers를 문자열로 변환한 후 반환한다.
# 4. 만약 numbers의 모든 원소가 0이라면 0을 반환한다.
# 시간 복잡도는 O(nlogn)이다.