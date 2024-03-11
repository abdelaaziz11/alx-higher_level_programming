#!/usr/bin/node
// factorial

const n = parseInt(process.argv[2]);

function factorialize (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorialize(num - 1);
  }
}

console.log(factorialize(n));
