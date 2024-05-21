#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    const characterNames = [];
    let charactersCount = 0;
    characters.forEach((characterUrl, index) => {
      request.get(characterUrl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          characterNames[index] = character.name;
          charactersCount++;
          if (charactersCount === characters.length) {
            characterNames.forEach(name => {
              console.log(name);
            });
          }
        }
      });
    });
  }
});
