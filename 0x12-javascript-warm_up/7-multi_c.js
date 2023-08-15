#!/usr/bin/node
let arg = process.argv[2];
if (arg === undefined || isNaN(arg)) {
	console.log('Missing number of occurrences');
} else {
	let ret = Number(arg);
	for (let i = 0; i < ret; i++) {
		console.log('C is fun');
	}
}
