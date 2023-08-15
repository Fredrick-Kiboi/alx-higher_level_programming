#!/usr/bin/node
function add(a, b) {
	return a + b;
}
let x = process.argv[2];
let y = process.argv[3];
console.log(add(x, y));
