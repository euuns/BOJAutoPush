const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .toString()
  .split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const v = Number(input[2]);

let result = 0;

for (let i = 0; i < n; i++) {
  if (arr[i] === v) {
    result++;
  }
}

console.log(result);
