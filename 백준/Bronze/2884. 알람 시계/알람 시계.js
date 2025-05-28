const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split(" ")
  .map(Number);
const H = input[0];
const M = input[1];

let hour = H;
let minute = M - 45;
if (minute < 0) {
  minute = 60 + minute;
  hour = H-1;
}

if (hour < 0) {
  hour = 23;
}

console.log(`${hour} ${minute}`);
