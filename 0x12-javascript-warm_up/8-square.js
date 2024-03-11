#!/usr/bin/node

const x = process.argv[2];

if (!isNaN(process.argv[2])) {
  let i = 0, j = 0;
  for (i = 0; i < x; i++) {
    for (j = 0; j < x; j++) {
      console.log('X');
    }
    console.log('X');
  }
}
