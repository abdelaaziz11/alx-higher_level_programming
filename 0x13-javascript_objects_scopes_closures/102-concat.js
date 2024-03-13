#!/usr/bin/node
const fs = require('fs');
const x = fs.readFileSync(process.argv[2], 'utf8');
const y = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], x + y);
