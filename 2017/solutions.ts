//
//  Day 3
//
//  Part 1
//

/*   ^
** y |
**   *-–>
**    x
*/

let dayThreeButton = document.getElementById('day3-button');
dayThreeButton.addEventListener("click", (e:Event) => dayThreeSolve());

let dayThreeSolve = () => {
  let solutionSpan = document.getElementById('day3-solution');
  let puzzleInput = <HTMLInputElement>document.getElementById('day3-input');
  let xCoordSpan = document.getElementById('day3-xCoord');
  let yCoordSpan = document.getElementById('day3-yCoord');

  let address = findMemoryAddress(+puzzleInput.value);
  console.log('memory address', address);
  let coord = CoordinatesForMemoryAddress(address);
  xCoordSpan.innerText = coord.x.toFixed();
  yCoordSpan.innerText = coord.y.toFixed();

  let distance = manhattanDistance(coord);
  solutionSpan.innerText = distance.toFixed();
}

let layerEdge = (num: number): number => (2*num+1)**2;

interface memoryLocation {
  layerIndex: number;
  remainder: number;
}

let findMemoryAddress = (memoryEntry: number): memoryLocation => {
  if (memoryEntry == 1) return { layerIndex: 0, remainder: 0 }
  for (let i = 1; i < memoryEntry; i++) {
    if (memoryEntry <= layerEdge(i)) {
      return {
        layerIndex: i,
        remainder: memoryEntry - layerEdge(i-1) - 1
      }
    }
  }
}

interface memoryCoordinates {
  x: number;
  y: number;
}

let CoordinatesForMemoryAddress = (location: memoryLocation): memoryCoordinates => {
  if (location.layerIndex == 0) return { x: 0, y: 0 };
  let remainder = location.remainder;
  let quadrantSize:number = (layerEdge(location.layerIndex) - layerEdge(location.layerIndex-1)) / 4.0;
  let xCoord = location.layerIndex;
  let yCoord = -location.layerIndex+1;
  if (remainder <= 0) return { x: xCoord, y: yCoord };
  for (let i = 0; i < quadrantSize-1; i++) {
    yCoord += 1;
    remainder -= 1;
    if (remainder <= 0) return { x: xCoord, y: yCoord };
  }
  for (let i = 0; i < quadrantSize; i++) {
    xCoord -= 1;
    remainder -= 1;
    if (remainder <= 0) return { x: xCoord, y: yCoord };
  }
  for (let i = 0; i < quadrantSize; i++) {
    yCoord -= 1;
    remainder -= 1;
    if (remainder <= 0) return { x: xCoord, y: yCoord };
  }
  for (let i = 0; i < quadrantSize; i++) {
    xCoord += 1;
    remainder -= 1;
    if (remainder <= 0) return { x: xCoord, y: yCoord };
  }
  return { x: xCoord, y: yCoord };
}

let manhattanDistance = (coord: memoryCoordinates): number => {
  return Math.abs(coord.x) + Math.abs(coord.y);
}

dayThreeSolve();

//
//  Part 1
//

interface memoryItem {
  coordinates: memoryCoordinates;
  value: number;
}

let adjacentMemory = (coord: memoryCoordinates): Array<memoryItem>
