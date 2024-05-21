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
 
    characters.forEach(characterUrl => { 
      request.get(characterUrl, function (error, response, body) { 
        if (error) { 
          console.error(error); 
        } else { 
          const character = JSON.parse(body); 
          console.log(character.name); 
        } 
      }); 
    }); 
  } 
}); 
