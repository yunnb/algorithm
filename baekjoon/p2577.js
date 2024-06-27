let input = require('fs').readFileSync('input.txt').toString().trim().split("\n");
let result = (input[0] * input[1] * input[2]).toString();
let countArr = Array.from({length: 10}, () => 0);

for (let i = 0; i < result.length; i++) countArr[+result.charAt(i)]++;
for (let i = 0; i < countArr.length; i++) console.log(countArr[i]);

