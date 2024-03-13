#!/usr/bin/node
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

const s = require('s');
const x = s.readFileSync(process.argv[2], 'utf8');
const y = s.readFileSync(process.argv[3], 'utf8');
s.writeFileSync(process.argv[4], x + y);
