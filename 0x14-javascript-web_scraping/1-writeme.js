#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');
const fpath = process.argv[2];
const fcontent = process.argv[3];
fs.writeFile(fpath, fcontent, 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});
