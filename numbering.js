const numbering = (num) => {
    let number = num.toString()
    if (number.length > 3){
        let result = ''
        let count = 0
        for(let i = number.length-4; i >= 0; i--){
            result = number[i] + result
            count += 1
            if (count === 2 && i!==0){
                result = ',' + result
                count = 0
            }
        }
        result = result + ',' + number.slice(number.length-3)
        console.log(result)
    }
    else{
        console.log(number)
    }
}

numbering(1235500)
