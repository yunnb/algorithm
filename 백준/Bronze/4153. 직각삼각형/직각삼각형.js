const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let i = 0;
do {
    const a = inputs[i].split(' ')[0] ** 2;
    const b = inputs[i].split(' ')[1] ** 2;
    const c = inputs[i].split(' ')[2] ** 2;
    const len = [a, b, c];

    len.sort(function (a, b) {
        return a-b;
    });

    if (len[2] === (len[0] + len[1])) console.log('right');
    else console.log('wrong');

    i++;
} while (inputs[i] !== "0 0 0");
