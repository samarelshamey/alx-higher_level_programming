#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');
const fpath = process.argv[2];
fs.readFile(fpath, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
