
input = `x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504`;

const xReg = /x=(\d+)\.?\.?(\d*)/;
const yReg = /y=(\d+)\.?\.?(\d*)/;

const clay = {
  xHash: {},
  addClay(x,y) {
    if (this.xHash[x] == undefined) { this.xHash[x] = {}; }
    this.xHash[x][y] = true;
  },
  isClayAt(x,y) {
    if (this.xHash[x] == undefined) { return false; }
    return this.xHash[x][y] == true;
  }
};

input.split('\n').forEach(function(l) {
  const [_x,firstX,endX] = l.match(xReg).map(parseFloat);
  const [_y,firstY,endY] = l.match(yReg).map(parseFloat);
  console.log(firstX, firstY);

  for (let i=firstX; i<endX+1 || i==firstX; i++) {
    for (let j=firstY; j<endY+1 || j==firstY; j++) {
      clay.addClay(i,j);
    }
  }
});
console.log(clay)


