#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonResults = JSON.parse(body).results;
    let counter = 0;
    for (const film of jsonResults) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
