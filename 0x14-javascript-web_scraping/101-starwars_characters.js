#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const urlFilms = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
let characters = [];

request.get(urlFilms, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  characters = data.characters;
  getChars(0);
});

const getChars = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const charData = JSON.parse(body);
    console.log(charData.name);
    getChars(index + 1);
  });
};
