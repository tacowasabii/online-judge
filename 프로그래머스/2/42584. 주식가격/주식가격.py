def solution(prices):
    answer = []
    dic = {}
    time = [0] * len(prices)
    
    for i, v in enumerate(prices):
        if i != len(prices) - 1:
            for j in range(i + 1, len(prices)):
                if v > prices[j]: 
                    time[i] = j - i
                    break
                if j == len(prices) - 1:
                    time[i] = j - i
                
    return time