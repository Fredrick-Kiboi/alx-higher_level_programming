#!/usr/bin/node
const numberOfArgs = process.argv.length - 2;

if (numberOfArgs === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
