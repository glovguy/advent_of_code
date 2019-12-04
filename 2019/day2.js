const input = require('./inputs').day2;

let head = 0;

while (head <= input.length) {
  const command = input[head];
  const firstNumIndex = input[head+1];
  const secondNumIndex = input[head+2];
  const destinationIndex = input[head+3];
  if (command === 1) {
    input[destinationIndex] = input[firstNumIndex] + input[secondNumIndex];
  } else if (command === 2) {
    input[destinationIndex] = input[firstNumIndex] * input[secondNumIndex];
  }

  head += 4;
}

console.log(input[0]);
