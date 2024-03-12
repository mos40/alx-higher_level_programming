// Create an empty object if w or h is not a positive integer or is 0
// Initialize the instance attributes with the provided values
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
