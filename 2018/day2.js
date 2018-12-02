const data = require('./day2_data');


//////////////
// Part One //
//////////////

function packages_checksum(packages) {
  const allCheckPairs = packages.map(package_checkpair).reduce(addPairs, [0,0]);
  return allCheckPairs[0] * allCheckPairs[1];
}

function package_checkpair(package) {
  const charCount = package_char_count(package);
  let doubles = 0;
  let triples = 0;
  for (char in charCount) {
    if (charCount[char] == 2) { doubles = 1; }
    if (charCount[char] == 3) { triples = 1; }
  }
  return [doubles, triples];
}

function package_char_count(package) {
  return package.split('').reduce((charCount, char) => {
    const isSet = charCount[char] != undefined;
    charCount[char] = isSet ? charCount[char]+1 : 1;
    return charCount;
  }, {});
}

function addPairs(a,b) { return [a[0]+b[0],a[1]+b[1]]; }

console.assert(packages_checksum(data)==7936, 'confirmed answer');
console.log(`Solution One: ${packages_checksum(data)}`);


//////////////
// Part Two //
//////////////

// Naive n^2 solution:

function find_pair_with_one_difference(packages) {
  for (let i=0; i<packages.length; i++) {
    const match = package_with_one_difference(packages[i], packages.slice(i+1,packages.length));
    if (match) { return [packages[i],match]; }
  }
}

function package_with_one_difference(p, compare) {
  for (let i=0; i<compare.length; i++) {
    if (has_one_difference(p,compare[i])) { return compare[i]; }
  }
  return null;
}

function has_one_difference(a,b) {
  let oneDiff = false;
  for (let i=0; i<a.length; i++) {
    if (a[i] == b[i]) { continue; }
    if (oneDiff) { return false; }
    oneDiff = true;
  }
  return true;
}

function remove_one_difference(pair) {
  let a = pair[0];
  let b = pair[1];
  for (let i=0; i<a.length; i++) {
    if (a[i] != b[i]) { return a.slice(0,i)+a.slice(i+1,a.length); }
  }
  throw 'something went wrong';
}

const pair = find_pair_with_one_difference(data);
const solutionTwo = remove_one_difference(pair);
console.assert(solutionTwo == 'lnfqdscwjyteorambzuchrgpx', 'confirmed second solution')
console.log(`Solution Two: ${solutionTwo}`);
