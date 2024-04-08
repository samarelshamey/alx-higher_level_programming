#!/usr/bin/node
const arg = process.argv[2];
let i = 0;
const x = parseInt(arg);

if (Number.isNaN(Number(arg))) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
