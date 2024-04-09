#!/usr/bin/node
const SquareX = require('./5-square.js');

class Square extends SquareX {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let txt = '';
      for (let j = 0; j < this.width; j++) { txt += c; }
      console.log(txt);
    }
  }
}
module.exports = Square;
