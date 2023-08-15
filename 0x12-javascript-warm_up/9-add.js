#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const arg = process.argv.length - 2;
if (arg === 0 || arg === 1) {
  console.log('NaN');
} else {
  const x = Number(process.argv[2]);
  const y = Number(process.argv[3]);
  const sum = add(x, y);
  console.log(sum);
}
