let input = require('fs').readFileSync('/dev/stdin').toString().trim();
let countArr = Array.from({length: 10}, () => 0);
for (let i = 0; i < input.length; i++) {
    let currentNum = input.charAt(i);

    if (currentNum === '6' || currentNum === '9') countArr[6] += 0.5;
    else countArr[currentNum]++;
}

let countMax= 0;
for (let i = 0; i < countArr.length; i++) {
    if (countArr[i] > countMax) countMax = countArr[i];
}
console.log(Math.ceil(countMax));