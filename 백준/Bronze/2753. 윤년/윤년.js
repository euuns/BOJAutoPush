const fs = require("fs");

const input = fs.readFileSync('/dev/stdin', 'utf8').trim();
const year = Number(input);

const result = (year%4===0 && year%100!==0) || year%400===0;
console.log(result?1:0);