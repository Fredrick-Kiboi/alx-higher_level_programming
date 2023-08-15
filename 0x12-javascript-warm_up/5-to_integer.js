#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  const ret = Number(arg);
  console.log('My number: ' + ret);
}
