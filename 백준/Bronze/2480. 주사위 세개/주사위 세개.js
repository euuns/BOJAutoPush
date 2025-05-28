const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split(" ")
  .map(Number);

const arr = [...new Set(input)];
const sortArr = input.sort((a, b) => b - a);

if (arr.length === 1) {
  console.log(10000 + arr[0] * 1000);
} else if (arr.length === 2) {
  console.log(1000 + sortArr[1] * 100);
} else {
  console.log(sortArr[0] * 100);
}
