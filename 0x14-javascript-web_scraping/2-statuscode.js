#!/usr/bin/node
// script that display the status code of a GET request
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
