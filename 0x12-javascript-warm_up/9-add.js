#!/usr/bin/node
function add(a, b) {
  return a + b;
}

let arg = process.argv.length - 2;
if (arg === 0 || arg === 1) {
	console.log('NaN')
} else {
	let x = Number(process.argv[2]);
	let y = Number(process.argv[3]);
	sum = add(x, y);
	console.log(sum);
}
