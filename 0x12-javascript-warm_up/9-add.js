#!/usr/bin/node
const x = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
function add (a, b) {
  return a + b;
}
console.log(x);
