#!/usr/bin/node
/*
class Rectangle {
  // Rectangle Class

  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || !isNaN(this.height) <= 0) {
      return {};
    }
    if (isNaN(this.height) || !isNaN(this.height)) {
      return {};
    
    }
  }
}
module.exports = Rectangle;
*/
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.width = undefined;
      this.height = undefined;
      return;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
