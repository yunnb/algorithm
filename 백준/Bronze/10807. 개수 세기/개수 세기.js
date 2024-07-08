const fs = require('fs');
const [n, input, x] = fs.readFileSync(0).toString().trim().split('\n');
const inputArr = input.trim().split(' ');

let cnt = 0;
for (let i = 0; i < inputArr.length ; i++) {
    if (inputArr[i] === x) cnt++;
}

console.log(cnt);