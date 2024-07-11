const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n');

const n = +inputs[0].trim();
for (let i = 1; i <= n; i++) {
    const count = Array.from(new Array(26), () => new Array(2).fill(0));
    const f = inputs[i].trim().split(' ')[0];
    const s = inputs[i].trim().split(' ')[1];
    let isPossible = "Possible";

    if (f.length === s.length) {
        for (let j = 0; j < f.length; j++) {
            count[f.charCodeAt(j) - 97][0]++;
            count[s.charCodeAt(j) - 97][1]++;
        }

        for (let j = 0; j < count.length; j++) {
            if (count[j][0] !== count[j][1]) {
                isPossible = "Impossible";
                break;
            }
        }
    }
    else isPossible = "Impossible";
    
    console.log(isPossible);
}