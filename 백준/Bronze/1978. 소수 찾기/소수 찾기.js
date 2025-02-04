const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const nums = inputs[1].split(' ').map(Number);

let cnt = 0;
for(let n of nums) {
    let isPrime = true;

    if (n === 1) continue;
    for (let i = 2; i < n; i++) {
        if (n <= 1 || n % i === 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) cnt++;
}

console.log(cnt);