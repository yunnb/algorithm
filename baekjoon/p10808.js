"use strict";

const input = require("fs").readFileSync("input.txt").toString().trim();
let countArr = new Array(26);

for (let i = 0; i < countArr.length ; i++) countArr[i] = 0;

for (let i = 0; i < input.length; i++) {
    let currentAlphabetIndex = input.charAt(i).charCodeAt() - 97;
    countArr[currentAlphabetIndex]++;
}

for (let i = 0; i < countArr.length; i++)
    process.stdout.write(countArr[i] + " ");


