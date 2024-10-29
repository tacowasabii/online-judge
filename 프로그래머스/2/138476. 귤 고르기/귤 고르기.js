function solution(k, tangerine) {
    const countMap = new Map()
    
    tangerine.forEach(v => {
        countMap.set(v, (countMap.get(v) || 0) + 1)
    })
    const arr = Array.from(countMap.values()).sort((a, b) => b - a)
    
    let ans = 0
    
    for (let v of arr){
        k -= v
        ans += 1
        if (k <= 0)
            return ans
    }
}