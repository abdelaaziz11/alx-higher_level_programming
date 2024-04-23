#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}):
