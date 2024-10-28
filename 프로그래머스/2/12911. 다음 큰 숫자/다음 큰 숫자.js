function solution(n) {
    const n_bin = n.toString(2)
    let cnt = 0
    for (let i = 0; i < n_bin.length; i++){
        if (n_bin[i] === '1'){
            cnt++
        }
    }

    n++
    while (1){
        let cnt2 = 0
        num_bin = n.toString(2)
        for (let i = 0; i < num_bin.length; i++){
            if (num_bin[i] === '1'){
                cnt2++
            }
        }
        if (cnt === cnt2){
            return n
        }
        n++
    }
}