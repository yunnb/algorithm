const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

let nums = inputs[1].trim().split(' ').map(Number);
nums.sort((a, b) => a - b);

console.log(nums[0], nums[nums.length-1]);