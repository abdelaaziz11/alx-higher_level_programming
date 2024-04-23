#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const urlFilms = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(urlFilms, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
