const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const T = Number(input[0]);

for(let i = 1; i <= T; i++){
  let cases = input[i].split(' ').map(Number);
  console.log(`Case #${i}: ${cases[0] + cases[1]}`)
}
