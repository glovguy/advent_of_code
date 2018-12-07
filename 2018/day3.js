

class Vector {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  is(other) { return this.x == other.x && this.y == other.y; }
  add(other) {
    return new Vector(this.x + other.x, this.y + other.y);
  }
}

class CompositeSurface {
  constructor(surfaces) {
    this.surfaces = surfaces;
    this._remove_dups();
  }
  _remove_dups() {
    for (let i=0; i<this.surfaces.length; null) {
      const otherSurfs = this.surfaces.slice(i+1,this.length);
      if (otherSurfs.length > 0 && otherSurfs.every(e => e.is(this.surfaces[i]))) {
        this.surfaces = [...this.surfaces.slice(0,i), ...this.surfaces.slice(i+1, this.surfaces.length)];
      } else {
        i++;
      }
    }
    return this;
  }
  get length() { return this.surfaces.length; }
  get isEmpty() { return this.surfaces.length == 0; }
  add(other) { return new CompositeSurface([...this.surfaces, ...other.surfaces]); }
  overlap(other) {
    const newSurfacesArrOfArrs = this.surfaces.map(rect => rect.overlap(other))
      .filter(r => !r.isEmpty).map(s => s.surfaces);
    const newSurfaces = flatten(newSurfacesArrOfArrs);
    return new CompositeSurface(newSurfaces);
  }
  get area() {
    if (this.surfaces.length == 0) { return 0; }
    const first = this.surfaces[0];
    const others = new CompositeSurface(this.surfaces.slice(1,this.surfaces.length));
    const totalOverlap = others.overlap(first);
    const overlapArea = (totalOverlap != undefined) ? totalOverlap.area : 0;
    const firstArea = first.area;
    const othersArea = others.area;
    return firstArea + othersArea - overlapArea;
  }
}

class Rect {
  constructor(x, y, width, height, id=undefined) {
    this.pos = new Vector(x,y);
    this.width = width;
    this.height = height;
    this.id = id;
  }
  is(other) {
    return this.pos.is(other.pos) && this.width == other.width && this.height == other.height;
  }
  get surfaces() { return Array.from([this]); }
  get left() { return this.pos.x; }
  get right() { return this.pos.x + this.width; }
  get top() { return this.pos.y; }
  get bottom() { return this.pos.y + this.height; }

  get area() { return this.width * this.height; }
  get isEmpty() { return (this.width == 0 && this.height == 0); }

  overlap(other) {
    return new CompositeSurface(other.surfaces.map(s => this.rect_overlap(s)).filter(s => !s.isEmpty));
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

function flatten(arr) {
  return [].concat.apply([], arr);
}

function data_from_puzzle_input() {
  const data = require('./day3_data');
  const rawDataRegex = /#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)/;
  const pf = parseFloat;
  const rects = data.map(d => {
    const raw = d.match(rawDataRegex);
    return new Rect(pf(raw[2]),pf(raw[3]),pf(raw[4]),pf(raw[5]),id=pf(raw[1]));
  });
  return rects;
}

// let rects = [
//   new Rect(1,3,4,4),
//   new Rect(3,1,4,4),
//   new Rect(5,5,2,2),
//   new Rect(3,3,2,2),
//   new Rect(4,3,1,2)
// ];
let rects = data_from_puzzle_input();


console.assert(new Vector(1,1).is(new Vector(1,1)), 'vector identity');
console.assert(new Vector(1,1).is(new Vector(1,2)) == false && new Vector(2,1).is(new Vector(1,1)) == false,
  'vector non-identity');

console.assert(new Rect(2,2,1,3).overlap(new Rect(2,2,1,3)).area == 3, 'overlap identical rect');
console.assert(new Rect(2,2,1,3).overlap(new Rect(2,2,1,2)).area == 2, 'overlap partial rect');
console.assert(new Rect(1,3,4,4).overlap(new Rect(3,1,4,4)).area == 4, 'overlap separate rect');
console.assert(new Rect(1,3,4,4).overlap(new CompositeSurface([new Rect(3,1,4,4)])).area == 4, 'overlap rect with composite surface');
console.assert(new CompositeSurface([new Rect(3,1,4,4)]).overlap(new Rect(1,3,4,4)).area == 4, 'overlap composite surface with rect');
console.assert(
  new Rect(1,3,4,4).overlap(new CompositeSurface([new Rect(3,1,4,4), new Rect(1,1,1,1), new Rect(7,7,1,1)])).area == 4,
  'overlap with composite surface containing extra rects');
console.assert(new Rect(2,2,1,3).is(new Rect(2,2,1,3)), 'rect identity');
console.assert(new Rect(2,2,1,3).is(new Rect(2,2,1,3)), 'rect non-identity');

const twoTwoOneThree = new CompositeSurface([new Rect(2,2,1,3)]);
const twoTwoOneTwo = new CompositeSurface([new Rect(2,2,1,2)]);
const oneThreeFourFour = new CompositeSurface([new Rect(1,3,4,4)]);
const threeOneFourFour = new CompositeSurface([new Rect(3,1,4,4)]);
const severalRects = new CompositeSurface([new Rect(3,1,4,4), new Rect(1,1,1,1), new Rect(7,7,1,1)]);
const severalIdenticalRects = new CompositeSurface([new Rect(3,1,4,4), new Rect(3,1,4,4), new Rect(3,1,4,4)]);
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

console.assert(
  severalIdenticalRects.surfaces.length == 1,
  'composite surface constructor removes duplicates');

// const totalOverlap = surface_self_overlapping(rects);
// console.log(`totalOverlap has ${totalOverlap.surfaces.length} rects`);
// console.log('if this number is large, the calculation will take a long time');
// console.log('going to calculate area now...');
// console.log(`Part One: ${totalOverlap.area}`);
// // confirmed answer for my data: 101781

const totalSurface = new CompositeSurface(rects);
const freeRect = rects.find((r, i) => rects.every((r2, i2) => i == i2 || r2.overlap(r).isEmpty));
console.log(`Part Two: ${freeRect.id}`);
