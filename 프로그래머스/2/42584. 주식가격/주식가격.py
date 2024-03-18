def solution(prices):
    answer = []
    dic = {}
    time = [0 for _ in range(len(prices))]
    
    for i, v in enumerate(prices):
        if i != len(prices) - 1:
            for j in range(i + 1, len(prices)):
                if v > prices[j]: 
                    time[i] = j - i
                    break
                if j == len(prices) - 1:
                    time[i] = j - i
                
    return time

# prices를 순회하면서 현재 가격보다 작은 가격이 나올 때까지의 시간을 구한다.
# 시간을 time에 저장한다.
# time을 반환한다.
# 시간 복잡도는 O(n^2)이다.

# 효용성 테스트 통과 못할줄 알았는데 했다!!