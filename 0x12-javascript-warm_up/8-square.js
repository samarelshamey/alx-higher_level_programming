#!/usr/bin/node
const arg = process.argv[2];
const x = parseInt(arg);
if (Number.isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
