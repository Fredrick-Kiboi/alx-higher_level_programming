#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < arg; x++) {
    let output = '';
    for (let y = 0; y < arg; y++) {
      output += 'X';
    }
    console.log(output);
  }
}
