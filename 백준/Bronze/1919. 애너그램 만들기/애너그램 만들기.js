const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n');

const count = Array.from(new Array(26), () => [0, 0]);
const f = inputs[0].trim();
const s = inputs[1].trim();
let cnt = 0;

for (let i = 0; i < f.length; i++) count[f.charCodeAt(i) - 97][0]++;
for (let i = 0; i < s.length; i++) count[s.charCodeAt(i) - 97][1]++;

for (let j = 0; j < count.length; j++) {
    if (count[j][0] !== count[j][1]) {
        if (count[j][0] === 0) cnt += count[j][1];
        else if (count[j][1] === 0) cnt += count[j][0];
        else cnt += Math.abs(count[j][0] - count[j][1]);
    }
}

console.log(cnt);