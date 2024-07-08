const fs = require('fs');
const [n, input, x] = fs.readFileSync(0).toString().trim().split('\n');
const inputArr = input.trim().split(' ');

inputArr.sort((a, b) => a - b);
let start = 0, end = inputArr.length - 1, cnt = 0;

while (start < end) {
    let a = +inputArr[start];
    let b = +inputArr[end];

    if (a + b === +x) {
        cnt++;
        start++;
    }
    else if (a + b < x) start++;
    else end--;
}
console.log(cnt);