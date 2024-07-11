const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n');

const n = +inputs[0].trim().split(' ')[0];
const k = +inputs[0].trim().split(' ')[1];

const s = [], y = [];
const student = Array.from(new Array(6), () => new Array(2).fill(0));
for (let i = 1; i < inputs.length; i++) {
    s[i-1] = +inputs[i].trim().split(' ')[0];
    y[i-1] = +inputs[i].trim().split(' ')[1];
    
    if (s[i-1] === 0) student[y[i-1]-1][0]++;
    else if (s[i-1] === 1) student[y[i-1]-1][1]++;
}

let room = 0;
for (let i = 0; i < student.length; i++) {
    room += Math.ceil(student[i][0] / k) + Math.ceil(student[i][1] / k);
}
console.log(room);