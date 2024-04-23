#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
