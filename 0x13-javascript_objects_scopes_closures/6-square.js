#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let txt = '';
      for (let j = 0; j < this.size; j++) { txt += 'c'; console.log(txt); }
    }
  }
}
module.exports = Square;
