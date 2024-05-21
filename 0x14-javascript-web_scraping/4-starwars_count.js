#!/usr/bin/node
// script that prints the number of movies
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const filmsData = JSON.parse(body).results;
  const moviesWithWedgeAntilles = filmsData.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  console.log(moviesWithWedgeAntilles.length);
});
