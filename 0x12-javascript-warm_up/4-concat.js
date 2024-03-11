#!/usr/bin/node

if (process.argv[2] === undefined) {
  if (process.argv[3] === undefined) {
    console.log('undefined' + ' is ' + 'undefined');
  } else {
    console.log('undefined' + ' is ' + process.argv[3]);
  }
} else {
  if (process.argv[3] === undefined) {
    console.log(process.argv[2] + ' is ' + 'undefined');
  } else {
    console.log(process.argv[2] + ' is ' + process.argv[3]);
  }
}
