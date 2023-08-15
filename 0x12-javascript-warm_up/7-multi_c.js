#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  const ret = Number(arg);
  for (let i = 0; i < ret; i++) {
    console.log('C is fun');
  }
}
