#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (err, data) => {
  if (err) {
    console.error(err);
  }
console.log(data);
});
