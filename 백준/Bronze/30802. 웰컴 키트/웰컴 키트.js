const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +inputs[0];
const size = inputs[1].split(' ').map(Number);
const count = inputs[2].split(' ').map(Number);

let shirts = 0;
for (const s of size) {
    shirts += Math.trunc(s / count[0]);
    if (s%count[0]!==0) shirts++;
}

const bundleOfPens= Math.trunc(n/count[1]);
const pens = n % count[1];

console.log(shirts);
console.log(bundleOfPens, pens);