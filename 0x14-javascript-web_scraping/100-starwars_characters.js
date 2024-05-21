#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
