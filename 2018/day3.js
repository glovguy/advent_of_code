

class Vector {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  add(other) {
    return new Vector(this.x + other.x, this.y + other.y);
  }
}

class CompositeSurface {
  constructor(surfaces) {
    this.surfaces = surfaces;
  }
  get length() { return this.surfaces.length; }
  add(other) { return new CompositeSurface([...this.surfaces, ...other.surfaces]); }
  union(other) {
    const newSurfaces = this.surfaces.map(rect => rect.union(other))
      .filter(r => r != undefined);
    return new CompositeSurface(newSurfaces);
  }
  get area() {
    if (this.surfaces.length == 0) { return 0; }
    const first = this.surfaces[0];
    const others = new CompositeSurface(this.surfaces.slice(1,this.surfaces.length));
    const totalUnion = others.union(first);
    const unionArea = (totalUnion != undefined) ? totalUnion.area : 0;
    return first.area + others.area - unionArea;
  }
}

class Rect {
  constructor(x, y, width, height) {
    this.pos = new Vector(x,y);
    this.width = width;
    this.height = height;
  }
  get surfaces() { return this; }
  get left() { return this.pos.x; }
  get right() { return this.pos.x + this.width; }
  get top() { return this.pos.y; }
  get bottom() { return this.pos.y + this.height; }

  get area() { return this.width * this.height; }

  union(other) {
    const left = Math.max(this.left,other.left);
    const right = Math.min(this.right,other.right);
    const top = Math.max(this.top,other.top);
    const bottom = Math.min(this.bottom,other.bottom);
    const width = right - left;
    const height = bottom - top;
    const rectExists = (width > 0 && height > 0);
    return rectExists ? new Rect(left, top, width, height) : undefined;
  }
}


// let rects = [
//   new Rect(1,3,4,4),
//   new Rect(3,1,4,4),
//   new Rect(5,5,2,2),
//   new Rect(3,3,2,2)
// ]

const data = require('./day3_data');
const rawDataRegex = /.*\@ (\d+),(\d+): (\d+)x(\d+)/;
const rects = data.map(d => {
  const raw = d.match(rawDataRegex);
  return new Rect(parseFloat(raw[1]),parseFloat(raw[2]),parseFloat(raw[3]),parseFloat(raw[4]));
});

let tallySurface = new CompositeSurface([])
for (let i=0; i<rects.length; i++) {
  const remainingRects = rects.slice(i+1,rects.length);
  const overlapSurface = new CompositeSurface(remainingRects).union(rects[i]);
  tallySurface = tallySurface.add(overlapSurface);
}

console.log(`tallySurface has ${tallySurface.surfaces.length} rects`);
console.log('if this number is large, the calculation will take a long time');
console.log('going to calculate area now...');
console.log(`Part One: ${tallySurface.area}`);
