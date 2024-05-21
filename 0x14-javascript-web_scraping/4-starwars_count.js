#!/usr/bin/node
// script that prints the number of movies
const request = require('request');
let n = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          n += 1;
        }
      });
    });
    console.log(n);
  }
});
