#!/usr/bin/node
const arg = process.argv.slice(2).map(Number);
if (arg.length <= 1) {
  console.log(0);
} else {
  const sec = arg.sort((a, b) => b - a)[1];
  console.log(sec);
}
