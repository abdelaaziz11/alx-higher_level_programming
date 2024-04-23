#!/usr/bin/node

const request = require('request');
const urlAPI = process.argv[2];

const IdWA = '18';

request.get(urlAPI, (err, response, body) => {
  if (err) {
    console.erroe(err);
  }
  let count = 0;
  const data = JSON.parse(body);

  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(IdWA)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
