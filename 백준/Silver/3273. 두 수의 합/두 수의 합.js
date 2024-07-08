const fs = require('fs');
const [n, input, x] = fs.readFileSync(0).toString().trim().split('\n');
const inputArr = input.trim().split(' ');

inputArr.sort((a, b) => a - b);
let left = 0, right = inputArr.length - 1, cnt = 0;

while (left < right) {
    let sum = +inputArr[left] + +inputArr[right];

    if (sum === +x) {
        cnt++;
        left++;
    }
    else if (sum < x) left++;
    else right--;
}
console.log(cnt);
