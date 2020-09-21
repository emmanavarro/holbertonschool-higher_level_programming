#!/usr/bin/node
// Class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
