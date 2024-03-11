#!/usr/bin/node

const x = process.argv[2];

if (!isNaN(process.argv[2])) {
  let i;
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
