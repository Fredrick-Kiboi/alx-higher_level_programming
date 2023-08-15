#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const x = process.argv[2];
const y = process.argv[3];
console.log(add(x, y));
