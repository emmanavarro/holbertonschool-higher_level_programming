#!/usr/bin/node
const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let letter = 0; letter < this.height; letter++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
