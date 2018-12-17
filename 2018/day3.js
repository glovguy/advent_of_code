
class Vector {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  add(other) { return new Vector(this.x + other.x, this.y + other.y); }
}

class CompositeSurface {
  constructor(surfaces) { this.surfaces = surfaces; }
  get length() { return this.surfaces.length; }
  get isEmpty() { return this.surfaces.length == 0; }
  get centroid() { return this.surfaces.map(r => r.centroid).reduce((a,b) => a+b); }
  add(other) { return new CompositeSurface([...this.surfaces, ...other.surfaces]); }
  overlap(other) {
    const newSurfaces = this.surfaces.map(r => r.overlap(other))
      .filter(s => s.length > 0)
      .reduce((arr,s) => [...arr, ...s.surfaces], []);
    return new CompositeSurface(newSurfaces);
  }
  get area() {
    if (this.surfaces.length == 0) { return 0; }
    const first = this.surfaces[0];
    const others = new CompositeSurface(this.surfaces.slice(1,this.surfaces.length));
    const totalOverlap = others.overlap(first);
    return first.area + others.area - totalOverlap.area;
  }
}

class Rect {
  constructor(x, y, width, height, id=undefined) {
    this.pos = new Vector(x,y);
    this.width = width;
    this.height = height;
    this.id = id;
  }
  get surfaces() { return [this]; }
  get centroid() {
    return new Vector(this.pos.x + this.width/2.0, this.pos.y + this.height/2.0);
  }
  get left() { return this.pos.x; }
  get right() { return this.pos.x + this.width; }
  get top() { return this.pos.y; }
  get bottom() { return this.pos.y + this.height; }

  get area() { return this.width * this.height; }
  get isEmpty() { return (this.width == 0 && this.height == 0); }

  overlap(other) {
    const newSurfaces = other.surfaces.map(s => this.rect_overlap(s))
      .filter(s => !s.isEmpty);
    return new CompositeSurface(newSurfaces);
  }

  rect_overlap(other) {
    const left = Math.max(this.left,other.left);
    const right = Math.min(this.right,other.right);
    const top = Math.max(this.top,other.top);
    const bottom = Math.min(this.bottom,other.bottom);
    const width = right - left;
    const height = bottom - top;
    const rectExists = (width > 0 && height > 0);
    return rectExists ? new Rect(left, top, width, height) : new Rect(0,0,0,0);
  }
}

function surface_self_overlapping(rects) {
  let tallySurface = new CompositeSurface([]);
  for (let i=0; i<rects.length; i++) {
    const remainingRects = rects.slice(i+1,rects.length);
    const overlapSurface = new CompositeSurface(remainingRects).overlap(rects[i]);
    tallySurface = tallySurface.add(overlapSurface);
  }
  return tallySurface;
}

function data_from_puzzle_input() {
  const data = require('./day3_data');
  const rawDataReg = /#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)/;
  return data.map(d => {
    const [_,id,x,y,width,height] = d.match(rawDataReg).map(parseFloat);
    return new Rect(x,y,width,height,id);
  });
}

// let rects = [
//   new Rect(1,3,4,4),
//   new Rect(3,1,4,4),
//   new Rect(5,5,2,2),
//   new Rect(3,3,2,2),
//   new Rect(4,3,1,2)
// ];
let rects = data_from_puzzle_input();


const testCentroid = new Rect(2,2,1,3).centroid;
console.assert(testCentroid.x == 2.5 && testCentroid.y == 3.5, 'rect centroid')
console.assert(new Rect(2,2,1,3).overlap(new Rect(2,2,1,3)).area == 3, 'overlap identical rect');
console.assert(new Rect(2,2,1,3).overlap(new Rect(2,2,1,2)).area == 2, 'overlap partial rect');
console.assert(new Rect(1,3,4,4).overlap(new Rect(3,1,4,4)).area == 4, 'overlap separate rect');
console.assert(new Rect(1,3,4,4).overlap(new CompositeSurface([new Rect(3,1,4,4)])).area == 4, 'overlap rect with composite surface');
console.assert(new CompositeSurface([new Rect(3,1,4,4)]).overlap(new Rect(1,3,4,4)).area == 4, 'overlap composite surface with rect');
console.assert(
  new Rect(1,3,4,4).overlap(new CompositeSurface([new Rect(3,1,4,4), new Rect(1,1,1,1), new Rect(7,7,1,1)])).area == 4,
  'overlap with composite surface containing extra rects');

const twoTwoOneThree = new CompositeSurface([new Rect(2,2,1,3)]);
const twoTwoOneTwo = new CompositeSurface([new Rect(2,2,1,2)]);
const oneThreeFourFour = new CompositeSurface([new Rect(1,3,4,4)]);
const threeOneFourFour = new CompositeSurface([new Rect(3,1,4,4)]);
const severalRects = new CompositeSurface([new Rect(3,1,4,4), new Rect(1,1,1,1), new Rect(7,7,1,1)]);
const severalIdenticalRects = new CompositeSurface([new Rect(3,1,4,4), new Rect(3,1,4,4), new Rect(3,1,4,4)]);
console.assert(twoTwoOneThree.centroid.x == 2.5 && twoTwoOneThree.centroid.y == 3.5, 'CompositeSurface centroid');
console.assert(
  twoTwoOneThree.overlap(twoTwoOneThree).area == 3,
  'overlap identical composite surfaces');
console.assert(
  twoTwoOneThree.overlap(twoTwoOneTwo).area == 2,
  'overlap partial composite surfaces');
console.assert(
  oneThreeFourFour.overlap(threeOneFourFour).area == 4,
  'overlap separate composite surfaces');
console.assert(
  oneThreeFourFour.overlap(severalRects).area == 4,
  'overlap with several rect composite surfaces');
console.assert(
  severalIdenticalRects.overlap(severalIdenticalRects).area == 16,
  'overlap identical multiple rect composite surfaces');

const totalOverlap = surface_self_overlapping(rects);
// console.log(`totalOverlap has ${totalOverlap.surfaces.length} rects`);
// console.log('if this number is large, the calculation will take a long time');
// console.log('going to calculate area now...');
// console.log(`Part One: ${totalOverlap.area}`);
// // confirmed answer for my data: 101781

const totalSurface = new CompositeSurface(rects);
const freeRect = rects.find((r, i) => rects.every((r2, i2) =>  i == i2 || r2.overlap(r).isEmpty));
console.log(`Part Two: ${freeRect.id}`);
// Confirmed answer: 909
